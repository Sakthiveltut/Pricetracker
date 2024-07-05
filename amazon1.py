from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.parse

driver = webdriver.Chrome()
driver.maximize_window()

aname = []
aprice = []
aimage = []
aoffer = []
aurl = []
aid=[]

c_url = "https://www.amazon.in/s?k=bluetooth+headphones&crid=164PTJHN96FKG&sprefix=%2Caps%2C200&ref=nb_sb_ss_recent_1_0_recent"

def aidFinder(url):
    aid = urllib.parse.unquote(url)
    aid=aid.split("dp/")[1]
    aid=aid.split("/")[0]
    return aid

def getLink(c_url):
     
    print("--------------------------------------------------------------------------------------------------------------")
    print("Name",len(aname))
    print("Price",len(aprice))
    print("Offer",len(aoffer))
    print("Image",len(aimage))
    print("Url",len(aurl))
    print("Id",len(aid))
    print("--------------------------------------------------------------------------------------------------------------")

    driver.get(c_url)
    product_elements = driver.find_elements(By.XPATH,"//div[@data-component-type='s-search-result']")
    for product_element in product_elements:

        if (product_element.find_elements(By.XPATH, ".//span[@class='a-price-whole']")):

            name_element = product_element.find_element(By.XPATH,".//h2/a")
            name = name_element.text
            name = str(name)
            name=name.replace("/","")
        
            url = name_element.get_attribute("href")

            price_element = product_element.find_element(By.XPATH,".//span[@class='a-price-whole']")
            price = price_element.text
            price = str(price).replace(",","")

            image_element = product_element.find_element(By.XPATH,".//img")
            image_link = image_element.get_attribute("src")

            offer_element = product_element.find_element(By.XPATH,".//span[@class='a-letter-space']")
            offer = offer_element.find_element(By.XPATH,"./following-sibling::span")
            
            #offer_element = product_element.find_element(By.XPATH, ".//div[@class='a-row a-size-base a-color-base']")
            #offer = offer_element.text.strip("")
            #offer = offer.split("(")[-1].replace(")","")

            if offer:
                aname.append(name)
                aurl.append(url)
                aoffer.append(offer.text)
                aprice.append(price)
                aimage.append(image_link)
                aid.append(aidFinder(url))

    next_button = driver.find_elements(By.CSS_SELECTOR,'.s-pagination-item.s-pagination-next.s-pagination-button')
    if (next_button):
        driver.find_element(By.XPATH, "//a[text()='Next']").click()
        c_url = driver.current_url
        getLink(c_url)
    
getLink(c_url)