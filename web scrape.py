import io
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#BeatifulSoup parse the html text
#opening the connection and grapping the info
my_url="eCommerece website url"
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
#html parser
page_soup=soup(page_html,"html.parser")

#grabs each product

containers=page_soup.findAll("div",{"class":"_3liAhj"})
filename="product.csv"
f=io.open(filename,"w",encoding="utf-8")
headers="ProductName , Rating , Price \n"
f.write(headers)
for container in containers:
    product=container.div.div.div.img["alt"]
    rating=container.findAll("div",{"class":"hGSR34 _2beYZw"})
    price=container.findAll("div",{"class":"_1vC4OE"})
    price_value=price[0].text
    
    try:
        rating_value=rating[0].text
    except IndexError:
        rating_value="No ratings "
    

    f.write(product + "," + rating_value[:-1] + "," + price_value[1:].replace(",","") +"\n")

f.close()
