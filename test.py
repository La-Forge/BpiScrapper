from BpiScrapper import Company
from pprint import pprint

company = Company("https://lehub.web.bpifrance.fr/startup/askhub")
pprint(company.getData())

#urlSource = "https://lehub.web.bpifrance.fr/search?advancedmode=1&refinementList%5Btechnologies%5D%5B0%5D=Intelligence%20Artificielle&refinementList%5Bmarkets%5D%5B0%5D=Technologie%20%26%20Telecommunications&page=1#listStartups"
#companies = Companies(urlSource)
#companies.extractCompanies(folder="./data/")
