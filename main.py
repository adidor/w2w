from bs4 import BeautifulSoup

with open('test.html','r') as html_file:
    content=html_file.read()

    soup=BeautifulSoup(content, 'lxml')
    for link in soup.find_all('a'):

        print(link.get('href'))
        print(link)
        print(link)

        

