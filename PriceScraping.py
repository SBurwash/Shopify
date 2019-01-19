#
# import csv as reader
#
# data_file = reader.
#     ("hopsandamltchb.csv")
# print(data_file[0:2])
import csv
from BeerElement import BeerElement
class BeerProgram:
    def __init__(self,fileName, rowType, rowName, rowPrice, rowWeight):
        self.compteur = 0
        self.rowType = rowType
        self.rowName = rowName
        self.rowPrice = rowPrice
        self.rowWeight = rowWeight
        self.elements = {}
        self.fileName = fileName

    #Obtenir le poid de la choppe a Barrock
    def getWeightChoppeB(self, string):
        weightO, tmp = string.split("g - ",1)
        return float(weightO)

    def getPriceChoppeB(self, string):
        tmp, priceO = string.split("g - ", 1)
        priceO = priceO[:-1]
        return float(priceO)

    def containsElement (self, name):
        for elem in self.elements:
            if elem == name:
                return True
        return False
    def addNewElement(self, type, name, stringPrice):
        price = self.getPriceChoppeB(stringPrice)
        weight = self.getWeightChoppeB(stringPrice)
        if not self.containsElement(name):
            self.elements[name] = BeerElement(type, name)
        self.elements[name].setPrice(weight, price)
    def readFile(self):
        firstLine = True
        with open(self.fileName) as f:

            reader = csv.reader(f)
            for row in reader:

                self.compteur = 0
                for element in row:
                    if not firstLine:
                        if self.compteur == self.rowType:
                            type = element
                        elif self.compteur == self.rowName:
                            name = element
                        elif self.compteur == self.rowPrice:
                            stringPrice = element
                            self.addNewElement(type, name, stringPrice)
                        self.compteur = self.compteur + 1
                firstLine = False



    def printElement(self):
        print("Houblon: \n")
        for name in self.elements:
            if(self.elements[name].Type == "houblon"):
                print("\n" + name)
                for weight in self.elements[name].Price:
                    print("\t"+ str(weight) + "g - " + str(self.elements[name].Price[weight]) + "$")
        print("\n Malt: ")
        for name in self.elements:
            if (self.elements[name].Type == "malt"):
                print("\n" + name)
                for weight in self.elements[name].Price:
                    print("\t" + str(weight) + "g - " + str(self.elements[name].Price[weight]) + "$")


    def getElements(self):
        return self.elements