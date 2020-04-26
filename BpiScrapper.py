from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pprint import pprint
import json
import os.path



class Company:
    def __init__(self, url):
        self.url = url
        self.keepDriver = False
        self.data = {}

    def getData(self):
        if not self.data:
            self.loadData()
        return self.data

    def loadData(self, existing_driver=None):
        try:
            driver = None
            if existing_driver:
                self.keepDriver = True
                driver = existing_driver
            else:
                self.keepDriver = False
                driver = webdriver.Chrome()

            # load page
            driver.get(self.url)

            # waiting page is loaded
            queryLogo = '//img[@class="sc-hzDkRC gPRpRG"]'
            button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, queryLogo)))

            self.data['identity'] = {}

            # extract logo
            self.data['identity']['logo'] = driver.find_element(
                By.XPATH, queryLogo).get_attribute('src')

            # extract siren adress
            siren_adress = driver.find_element(
                By.XPATH, '//div[contains(@class,"startup__identity")]/div[1]')
            parts = siren_adress.text.split("\n")
            self.data['identity']['siren'] = parts[0].split(":")[1].strip()
            adress = ""
            for row in parts[1:]:
                adress += row + "\n"
            self.data['identity']['adress'] = adress[:-1]

            # extract links
            links = driver.find_elements(
                By.XPATH, '//div[contains(@class,"startup__identity")]/div[1]/div/a')
            for link in links:
                url = link.get_attribute('href')
                if 'twitter' in url:
                    self.data['identity']['twitter'] = url
                elif 'linkedin' in url:
                    self.data['identity']['linkedin'] = url
                else:
                    self.data['identity']['website'] = url

            # extract technologies
            self.data['identity']['technologies'] = []
            for tech in driver.find_elements(By.XPATH, '//div[contains(@class,"startup__identity")]/div[2]/div[1]/div'):
                self.data['identity']['technologies'].append(tech.text)

            # extract jobs
            self.data['identity']['jobs'] = []
            for job in driver.find_elements(By.XPATH, '//div[contains(@class,"startup__identity")]/div[3]/div/div'):
                self.data['identity']['jobs'].append(job.text)

            # extract market
            self.data['identity']['market'] = []
            for market in driver.find_elements(By.XPATH, '//div[contains(@class,"startup__identity")]/div[4]/div/div/div'):
                self.data['identity']['market'].append(market.text)

            # extract business model
            self.data['identity']['business_model'] = []
            for bm in driver.find_elements(By.XPATH, '//div[contains(@class,"startup__identity")]/div[5]/div/div'):
                self.data['identity']['business_model'].append(bm.text)

            # extract locations
            self.data['identity']['locations'] = []
            for location in driver.find_elements(By.XPATH, '//div[contains(@class,"startup__identity")]/div[6]/div/div/div'):
                self.data['identity']['locations'].append(location.text)

            # extract name
            self.data['identity']['name'] = driver.find_element(
                By.XPATH, '//div[contains(@class,"startup__presentation")]/div[1]/h1').text

            # extract description
            self.data['identity']['description'] = driver.find_element(
                By.XPATH, '//div[contains(@class,"startup__presentation")]/p').text

            # extract description
            self.data['identity']['creation'] = driver.find_element(
                By.XPATH, '//div[contains(@class,"startup__presentation")]/div[last()]/div[1]/div[2]').text

            # extract description
            self.data['identity']['headcount'] = driver.find_element(
                By.XPATH, '//div[contains(@class,"startup__presentation")]/div[last()]/div[2]/div[2]').text


            # extract products
            if (len(driver.find_elements(By.XPATH, '//div[contains(@class,"startup__products")]'))>0):
                self.data['products'] = {
                    'title': driver.find_element(By.XPATH, '//div[contains(@class,"startup__products")]/div[2]/div/div/div[1]').text,
                    'description': driver.find_element(By.XPATH, '//div[contains(@class,"startup__products")]/div[2]/div/div/div[2]').text
                }

            # extract team
            self.data['team'] = []
            for person in driver.find_elements(By.XPATH, '//div[contains(@class,"startup__team")]/div[2]/a'):
                self.data['team'].append({
                    'name': person.find_element(By.XPATH, 'div/div[1]').text,
                    'function': person.find_element(By.XPATH, 'div/div[2]').text
                })

        finally:
            if self.keepDriver == False:
                print("Quit driver after company loading")
                driver.quit()


class Companies:
    def __init__(self, url):
        self.url = url

    def extractCompanies(self, folder):
        driver = webdriver.Chrome()
        # load page
        driver.get(self.url)

        query = '//button[text()="Charger plus"]'
        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, query)))
        SCROLL_PAUSE_TIME = 0.5

        while True:
            btns = driver.find_elements(By.XPATH, query)
            if len(btns) > 0:
                # scroll to the bottom of the page
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                print("loading more companies")
                btns[0].click()
                time.sleep(SCROLL_PAUSE_TIME)
            else:
                break

        # extract links
        links = driver.find_elements(By.XPATH, '//a[@class="sc-jbKcbu JjNx"]')
        #data = []
        for link in links:
            url = link.get_attribute("href")
            id = url.split("/")[-1]
            filename = folder+id+".json"
            if os.path.exists(filename):
                print("already scraped " + url)
            else:
                print('loading company ' + url)
                company = Company(url)
                with open(filename, 'w') as outfile:
                    json.dump(company.getData(), outfile)
                time.sleep(SCROLL_PAUSE_TIME)


        print("Quit driver for companies")
        driver.quit()


if __name__ == '__main__':
    urlSource = "https://lehub.web.bpifrance.fr/search?advancedmode=1&refinementList%5Btechnologies%5D%5B0%5D=Intelligence%20Artificielle&refinementList%5Bmarkets%5D%5B0%5D=Technologie%20%26%20Telecommunications&page=1#listStartups"
    companies = Companies(urlSource)
    companies.extractCompanies(folder="./data/")


    #Company('https://lehub.web.bpifrance.fr/startup/hidden-market').getData()
