from bs4 import BeautifulSoup
import urllib.request
 

def get_html(url):
	response = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
	)
	f = urllib.request.urlopen(response)
	return f.read()

def parse(page):
	soup = BeautifulSoup(page, 'lxml')
	tab1 = soup.find('div', class_="wtab swtab", id="tab_wdaily1")
	weather1 = tab1.find('div', class_="temp")
	minimum = weather1.find("span", class_="value m_temp c").text
	weather2 = weather1.find("em")
	maximum = weather2.find("span", class_="value m_temp c").text
	print('Прогноз погоды на сегодня: ' '\n' 'Максимально ' + maximum + '°C' '\n' 'Минимально ' + minimum + '°C')

def main():
	parse(get_html('https://www.gismeteo.ua/weather-synelnykove-12357/'))

if __name__ == '__main__':
	main()