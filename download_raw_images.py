from utils.crawler import EbirdCrawler

if __name__ == '__main__':

    url = "https://media.ebird.org/catalog?taxonCode=formag1&mediaType=photo&sort=rating_rank_desc"
    class_name = "taiwan-blue-magpie"
    # url = "https://media.ebird.org/catalog?taxonCode=rbbmag&mediaType=photo&sort=rating_rank_desc"
    # class_name = "red-billed-blue-magpie"
    # url = "https://media.ebird.org/catalog?taxonCode=gobmag1&mediaType=photo&sort=rating_rank_desc"
    # class_name = "yellow-billed-blue-magpie"
    
    ebird_crawler = EbirdCrawler(url, class_name, max_image_num=1500)
    ebird_crawler.scrape_images()