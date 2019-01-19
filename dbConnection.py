from PriceScraping import BeerProgram
fileName = "hopsandamltchb.csv"
ps = BeerProgram(fileName, 2, 6, 7, None)
ps.readFile()
myElem = ps.elements

class dbConnection:
    def __init__(self, listOfElements):
        self.ourElem = listOfElements

