import scrapy
from ..items import AmazondatascrapingItem

class AmazondataSpider(scrapy.Spider):
    name = 'amazondata'
    start_urls = ["https://www.amazon.in/s?k=books&ref=nb_sb_noss_1"]
    count=2

    def parse(self, response):
        Item=AmazondatascrapingItem()

        #All book sections will be selected now
        all_books=response.css(".s-result-item.s-asin.sg-col-0-of-12.sg-col-16-of-20.sg-col.s-widget-spacing-small.sg-col-12-of-16")
        # all_books=response.xpath("//div[@class=s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16]/text()")
        # print(f"All BOOOOKKKKKK:{all_books}")

        #For loop will extract the indivisual book data from each section
        for books in all_books:

            item_title=books.css("div.s-card-container.s-overflow-hidden.aok-relative.puis-include-content-margin.s-latency-cf-section.s-card-border").css(".a-size-medium.a-color-base.a-text-normal::text").extract_first()
            # item_title=books.css(".a-size-medium.a-text-normal").css("::text").extract()
            # print(f"TITLEeeeeeeeeekkkkkkkkk:{item_title}")

            item_author=books.css(".a-size-base.a-link-normal.s-underline-text.s-underline-link-text.s-link-style").css("::text").extract_first()
            # print(f"AUTHORRRR:{item_author}")

            item_price=books.css(".a-price-whole").css("::text").extract_first()
            # print(f"PRICE:{item_price}")

            item_image=books.css(".a-section.aok-relative.s-image-fixed-height").css(".s-image::attr(src)").extract_first()
            # print(f"Image:{item_image}")

            item_link=books.css(".a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal").css("::attr(href)").extract_first()
            # print(f"ITEM LINK:{item_link}")

            Item["item_title"]=item_title
            Item["item_author"]=item_author
            Item["item_price"]=item_price
            Item["item_image"]=item_image
            Item["item_link"]=item_link

            yield Item

            AmazondataSpider.start_urls= "https://www.amazon.in/s?k=books&page="+str(AmazondataSpider.count)+"&qid=1662730572&ref=sr_pg_2"
            AmazondataSpider.count+=1
            #If you want to scrap first 1000 pages put a if condition
            # if AmazondataSpider.count<=1000:
            #     yield response.follow(AmazondataSpider.start_urls,callback=self.parse)
            
            yield response.follow(AmazondataSpider.start_urls,callback=self.parse)

