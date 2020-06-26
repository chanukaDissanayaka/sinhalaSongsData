import scrapy
import requests
from scrapy.spiders import SitemapSpider
from scrapy.http.request import Request
from scrapy.selector import HtmlXPathSelector
import re


class SongBookSpider(scrapy.Spider):
    name = "SongBook"
    allowed_domains = ["sinhalasongbook.com"]
    #sitemap_urls = ["https://sinhalasongbook.com/lyrics-sitemap.xml"]
    start_urls   = ["https://sinhalasongbook.com/all-sinhala-song-lyrics-and-chords/?_page="+str(i) for i in range(1, 22)]

    #sitemap_rules = [('^(?!.*artist).*$', 'parse')]
    count = 0

    '''def start_requests(self):
        urls = ["https://sinhalasongbook.com/all-sinhala-song-lyrics-and-chords/?_page="+str(i) for i in range(1, 22)]
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)'''

    def parse1(sefl, response):
        hxs = HtmlXPathSelector(response)
        return hxs

    def parse_song_details(self, response):
        song_page = response
        
        title_mix = (song_page.xpath('//div[@class="entry-content"]/h2/text()')).get()
        title_sin = (song_page.xpath('//span[@class="sinTitle"]/text()')).get()

        artist = song_page.xpath('//div[@class="su-row"]//span[@class="entry-categories"]//a/text()').extract()
        separator = ', '
        artist_data = (separator.join(artist))
        
        genre = song_page.xpath('//div[@class="su-row"]//span[@class="entry-tags"]//a/text()').extract()
        separator = ', '
        genre_data = (separator.join(genre))
        
        writer = song_page.xpath('//div[@class="su-row"]//span[@class="lyrics"]//a/text()').extract()
        separator = ', '
        writer_data = (separator.join(writer))
        
        music  = song_page.xpath('//div[@class="su-row"]//span[@class="music"]//a/text()').extract()
        separator = ', '
        music_data = (separator.join(music))

        '''title_mix = song_page.xpath('//div[@class="entry-content"]/h2/text()').extract()
        title_sin = song_page.xpath('//span[@class="sinTitle"]/text()').extract()

        artist = song_page.xpath('//div[@class="su-row"]//span[@class="entry-categories"]//a/text()').extract()
        genre = song_page.xpath('//div[@class="su-row"]//span[@class="entry-tags"]//a/text()').extract()
        writer = song_page.xpath('//div[@class="su-row"]//span[@class="lyrics"]//a/text()').extract()
        music  = song_page.xpath('//div[@class="su-row"]//span[@class="music"]//a/text()').extract()'''

        songBody = (song_page.xpath('//div[@class="entry-content"]//pre/text()').extract())

        songBodySplit = []
        for parts in songBody:
            lines = parts.split('\n')
            for line in lines:
                songBodySplit.append(line)
        
        
        song = ""
        chords = ""

        for line in songBodySplit:
            if(re.search('[a-zA-Z]', line)):
               chords = chords + line
            else:
                line = line.replace('+','')
                line = line.replace('|','')
                song = song + " " + line
                song.strip()
        
        #print(song)
                
        yield {
            'title_mix': title_mix,
            'title_sin': title_sin,
            'artist' : artist_data,
            'genre' : genre_data,
            'writer' : writer_data,
            'music' : music_data,
            'song' : song,
        }
        

    def parse(self, response):
        #songTitles = response.xpath('//*[@class="entry-title-link"]/text()').extract()
        #songhref = response.xpath('//*[@class="entry-title-link"]/@href').extract()

        songhref = response.xpath('//div[@class="col-md-6 col-sm-6 col-xs-12 pt-cv-content-item pt-cv-1-col"]//a/@href').extract()
        print(songhref)

        for song in songhref:
            #print(title)
            #songPageBody = Request(song, callback=self.parse1)
            #print(songPageBody)
            #songPageBody = requests.get(song)
            #song_page = BeautifulSoup(songPageBody.content, 'lxml')
            self.count = self.count + 1
            yield scrapy.Request(
                song,
                callback=self.parse_song_details
            )


            #artist = songPageBody.xpath('//div[@class="su-row"]/span').extract()
            
            #title = songPageBody.xpath('//div[@class="entry-content"]/h2/text()').extract()
            #artist = songPageBody.xpath('//div[@class="su-row"]/span[@class="entry-categories"]/text()').extract()
            #print(title)
            
            '''artist = songPageBody.xpath('//div[@class="su-row"]/span[@class="entry-categories"]/text()').extract()
            artist = songPageBody.xpath('//div[@class="su-row"]/span[@class="entry-categories"]/text()').extract()
            artist = songPageBody.xpath('//div[@class="su-row"]/span[@class="entry-categories"]/text()').extract()
            artist = songPageBody.xpath('//div[@class="su-row"]/span[@class="entry-categories"]/text()').extract()
            artist = songPageBody.xpath('//div[@class="su-row"]/span[@class="entry-categories"]/text()').extract()'''
            
        

        '''for l in song_lines:
            song_line = l.split('\n')[1].strip()
            song = song + " " + song_line'''

        '''yield{
            'title' : response.xpath('//*[@id="lyricsTitle"]/h2/text()')[0].get().split(' - ')[0],
            'singer': response.xpath('//*[@id="lyricsTitle"]/h2/text()')[0].get().split(' - ')[1],
            'song' : song
            }'''

        print("-----------------------count--------", self.count)
