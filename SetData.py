import requests
import csv
import json

class SetData:

    def __init__(self, year):
        self.date = []
        self.fermeture = []
        self.ouverture = []
        self.highest = []
        self.lowest = []
        self.volume = []
        self.variation = []
        #f_and_g
        self.greed_fear = []
        #call_put
        self.priceList = []
        self.longShortRateList = []
        self.dateList = []
        self.year = year
        self.read_file()
        if len(self.date) > 1000:
            self.get_greed_fear(1000)
        else:
            self.get_greed_fear(len(self.date))


    @staticmethod
    def price_to_float(row):
        return float(row.replace('.', '').replace(',', '.'))

    def read_file(self):
        with open('bitcoin_data_' + self.year + '.csv', 'r+') as f:
            reader = csv.reader(f)
            for row in reader:
                self.date.append(row[0])
                self.fermeture.append(SetData.price_to_float(row[1]))
                self.ouverture.append(SetData.price_to_float(row[2]))
                self.highest.append(SetData.price_to_float(row[3]))
                self.lowest.append(SetData.price_to_float(row[4]))
                self.volume.append(row[5])
                self.variation.append(float(row[6].replace('%', '').replace(',', '.')))

            if len(self.date) > 1000:
                for i in range (0, len(self.date)-1000):
                    self.variation.pop()
                    self.ouverture.pop()
                    self.fermeture.pop()

            self.variation.reverse()
            self.ouverture.reverse()
            self.fermeture.reverse()

    def get_greed_fear(self, nbr_days):
        get_request = requests.get('https://api.alternative.me/fng/?limit=' + str(nbr_days))
        result = json.loads(get_request.text)
        for entry in result['data']:
            self.greed_fear.append(int(entry['value']))
        self.greed_fear.reverse()
    
    def get_call_put(self, interval):
        url = "http://open-api.coinglass.com/api/pro/v1/futures/longShort_chart?interval=" + str(interval) + "&symbol=BTC"
        #https://open-api.coinglass.com/api/pro/v1/futures/longShort_chart?symbol=BTC&interval=2
        params = {}
        headers = {
        'coinglassSecret': '8266a28d6e084e1bb28b9fb17d682582'
        }
        get_request = requests.get(url, headers=headers, data = params)
        result = json.loads(get_request.text)
        self.priceList = result['data']['priceList']
        self.longShortRateList = result['data']['longShortRateList'] #longRateList/shortsRateList
        self.dateList = result['data']['dateList'] #in epoch

        #volume
        url= "https://open-api.coinglass.com/api/pro/v1/futures/openInterest/chart?symbol=BTC&interval=4"
        get_request = requests.get(url, headers=headers, data = params)
        result = json.loads(get_request.text)
        print(result)
    
    def display(self, l):
        for s in l:
            print(str(s).replace(".", ","))
        
        



#data = SetData("2019-2022")
#print("=========4h==========")
#data.get_call_put(5)
