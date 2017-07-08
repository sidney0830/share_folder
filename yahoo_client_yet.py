import time
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Firefox() # chrome瀏覽器
time.sleep(0.1)

driver.get('http://store.steampowered.com/search/?filter=topsellers')

#            
# elem=driver.find_element_by_css_selector('rank1.rank') 
# elem=driver.find_elements_by_class_name("recmdbillboard tabview")
# driver.find_element_by_link_text("暢銷商品").click()



html_source = driver.page_source
driver.quit()  # close bowser
print ('Browser closed')


soup = BeautifulSoup(html_source, 'xml')
item_data = soup.find_all(class_="rank1 rank")

time.sleep(3)	


# str1 = ''.join(str(e) for e in elem)
# print ('elem='+ elem)
# print(soup, file=open("yahootxt.txt", "w"))
print(soup)

