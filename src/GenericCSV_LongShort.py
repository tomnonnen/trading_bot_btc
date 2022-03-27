from backtrader.feeds import GenericCSVData

class GenericCSV_LongShort(GenericCSVData):

    # Add a 'lsratio' line to the inherited ones from the base class
    lines = ('longshortratio',)

    # openinterest in GenericCSVData has index 7 ... add 1
    # add the parameter to the parameters inherited from the base class
    params = (('longshortratio', 8),)