import urllib.request as urllib2
from bs4 import BeautifulSoup
import pandas as pd
import re
import csv
from unidecode import unidecode

f1 = 'http://metrolyrics.com/maroon-5-alpage-1'
f2 = 'http://metrolyrics.com/maroon-5-alpage-2'
f3 = 'http://metrolyrics.com/maroon-5-alpage-3'
#fetch_page = 'http://metrolyrics.com/{}-lyrics-maroon-5.html'
quote_page = 'http://metrolyrics.com/{}-maroon-5.html'
filename = 'maroon5-songs.csv'
# songs = pd.read_csv(filename)
songfile = open(filename, 'w')
wr = csv.writer(songfile)
wr.writerow(["song"])

def getsongs(fp,fetch_page):
    songlist = []
    page = urllib2.urlopen(fetch_page)
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find('table', {'class':"songs-table compact"})
    links = table.findAll('a',text =True)
    urllist = []
    for link in links:
        urllist.append(link.get('href'))
    urllist = list(urllist)
    # print (urllist)

    strlinks = list(map(str, links))
    # print(strlinks)
    names = re.compile(r'>[\w|\W]+<\/a>')
    for link in strlinks:
        match = names.search(link).group(0)
        match = match.replace('>\n','')
        match = match.replace('\n</a>', '')
        match = match.replace(' Lyrics', '')
        songlist.append(match)

    for song in list(songlist):
        fp.writerow([song])

    return songlist, urllist

def getlyrics(file):
    songs = pd.read_csv(file)
    # for index, row in songs.iterrows():
    for index, url in enumerate(urllist):
        # urlsong = row['song'].lower().replace(' ', '-')
        # url = quote(quote_page.format(urlsong.encode(encoding='ascii')))
        # url = quote_page.format(urlsong)
        # print (url)
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        verses = soup.find_all('p', attrs={'class': 'verse'})

        lyrics = ''

        for verse in verses:
            text = verse.text.strip()
            text = re.sub(r"\[.*\]\n", "", unidecode(text))
            if lyrics == '':
                lyrics = lyrics + text.replace('\n', '|-|')
            else:
                lyrics = lyrics + '|-|' + text.replace('\n', '|-|')

        songs.at[index, 'lyrics'] = lyrics

        print('saving {}'.format(songlist[index]))
        songs.head()
    return songs



if __name__ == "__main__":
    songlist1, urllist1 = getsongs(wr,f1)
    songlist2, urllist2 = getsongs(wr,f2)
    songlist3, urllist3 = getsongs(wr,f3)
    songlist = songlist1+songlist2+songlist3
    urllist = urllist1+urllist2+urllist3
    songfile.close()
    songs = getlyrics(filename)
    print('writing to .csv')
    songs.to_csv(filename, sep=',', encoding='utf-8')

