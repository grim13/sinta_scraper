import requests
from bs4 import BeautifulSoup

def schollar(id) :
    url = 'https://sinta.kemdikbud.go.id/authors/profile/'+str(id)+'/?view=googlescholar'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    datas = soup.find_all(class_="ar-list-item mb-5")
    results = []
    for data in datas:
        results.append({
            'title': data.find(class_="ar-title").find('a').get_text().strip(' '),
            'href': data.find(class_="ar-title").find('a').attrs['href'.strip(' ')],
            'authors': data.find(class_="ar-meta").find('a').get_text().strip(' '),
            'year': data.find(class_="ar-year").get_text().strip(' '),
            'publisher': data.find(class_="ar-pub").get_text().strip(' '),
            'cited': data.find(class_="ar-cited").get_text().strip(' ')
        })
    return results

def scopus(id) :
    url = 'https://sinta.kemdikbud.go.id/authors/profile/'+str(id)+'/?view=scopus'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    datas = soup.find_all(class_="ar-list-item mb-5")
    results = []
    for data in datas:
        results.append({
            'title': data.find(class_="ar-title").find('a').get_text().strip(' '),
            'href': data.find(class_="ar-title").find('a').attrs['href'.strip(' ')],
            'authors': data.find(class_="ar-meta").find('a').get_text().strip(' '),
            'year': data.find(class_="ar-year").get_text().strip(' '),
            'publisher': data.find(class_="ar-pub").get_text().strip(' '),
            'cited': data.find(class_="ar-cited").get_text().strip(' ')
        })
    return results

def garuda(id) :
    url = 'https://sinta.kemdikbud.go.id/authors/profile/'+str(id)+'/?view=garuda'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    datas = soup.find_all(class_="ar-list-item mb-5")
    results = []
    for data in datas:
        results.append({
            'title': data.find(class_="ar-title").find('a').get_text().strip(' '),
            'href': data.find(class_="ar-title").find('a').attrs['href'.strip(' ')],
            'authors': data.find(class_="ar-meta").find('a').get_text().strip(' '),
            'year': data.find(class_="ar-year").get_text().strip(' '),
            'publisher': data.find(class_="ar-pub").get_text().strip(' '),
            'cited': data.find(class_="ar-cited").get_text().strip(' ')
        })
    return results

def wos(id) :
    url = 'https://sinta.kemdikbud.go.id/authors/profile/'+str(id)+'/?view=wos'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    datas = soup.find_all(class_="ar-list-item mb-5")
    results = []
    for data in datas:
        results.append({
            'title': data.find(class_="ar-title").find('a').get_text().strip(' '),
            'href': data.find(class_="ar-title").find('a').attrs['href'.strip(' ')],
            'authors': data.find(class_="ar-meta").find('a').get_text().strip(' '),
            'year': data.find(class_="ar-year").get_text().strip(' '),
            'publisher': data.find(class_="ar-pub").get_text().strip(' '),
            'cited': data.find(class_="ar-cited").get_text().strip(' ')
        })
    return results

def rama(id) :
    url = 'https://sinta.kemdikbud.go.id/authors/profile/'+str(id)+'/?view=rama'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    datas = soup.find_all(class_="ar-list-item mb-5")
    results = []
    for data in datas:
        results.append({
            'title': data.find(class_="ar-title").find('a').get_text().strip(' '),
            'href': data.find(class_="ar-title").find('a').attrs['href'.strip(' ')],
            'authors': data.find(class_="ar-meta").find('a').get_text().strip(' '),
            'year': data.find(class_="ar-year").get_text().strip(' '),
            'publisher': data.find(class_="ar-pub").get_text().strip(' '),
            'cited': data.find(class_="ar-cited").get_text().strip(' ')
        })
    return results