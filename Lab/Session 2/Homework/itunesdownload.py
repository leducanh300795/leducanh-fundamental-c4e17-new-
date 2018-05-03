from urllib.request import urlopen
from bs4 import BeautifulSoup
from youtube_dl import YoutubeDL
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"
#1.1 Open connection
conn = urlopen(url)
#1.2 Read data
raw_data= conn.read()
#1.3 Decode
text = raw_data.decode('utf8')

itunes_file= open("itunes.html", "wb") #w la text ko, wb la data thô chưa được giải mã
itunes_file.write(raw_data)
itunes_file.close()

soup = BeautifulSoup(text, "html.parser") #coi doan van nhu html

div= soup.find("div", id = "main")
ul= div.find("ul")
li_list = ul.find_all("li")
li = li_list[0]
song_list = []

for li in li_list:
    a_song= li.h3.a
    a_artist= li.h4.a
    a_namesong = a_song.string
    a_nameartist = a_artist.string
    # print(a_namesong)
    # print(a_nameartist)
    # print("------------------------------------------")
    item = {
        "Names": a_namesong,
        "Artists": a_nameartist
    }
    song_list.append(item)
# title = a['title']
# print(tittle)
#3.
# print(item_list)
pyexcel.save_as(records=song_list, dest_file_name="itunes.xlsx")

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the second entry (video)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
for li in li_list:
    song = item['Names']
    dl.download([song])
# dl = YoutubeDL(options)
#
# dl.download([song.item['Names']])
