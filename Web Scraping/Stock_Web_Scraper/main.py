from bs4 import BeautifulSoup
import requests

print('Please enter a stock ticker or multiple stock tickers! Enter stop to finish queries!')
stockTicker = input()
try:
    html_text = requests.get(
        f'https://finance.yahoo.com/quote/{stockTicker}?p={stockTicker}').text
    soup = BeautifulSoup(html_text, 'lxml')
    stock_price_html_elem = soup.find_all(
        class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")
    print(stock_price_html_elem)
    stock_price = stock_price_html_elem[0].decode_contents()
    if(len(stock_price) == 0):
        raise Exception()
    else:
        print(f'{stockTicker} is at a price of {stock_price}')
except:
    print('Incorrect stock ticker')
