

from PriceScraping import BeerProgram

fileName = "hopsandamltchb.csv"
ps = BeerProgram(fileName, 2, 6, 7, None)

ps.readFile()
ps.printElement()
