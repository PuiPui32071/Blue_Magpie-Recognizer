import os

from icrawler.builtin import GoogleImageCrawler


def crawl(model: int, amount: int = 1000):
    path: str = f'./dataset/iphone-{str(model)}'
    if not os.path.exists(path):
        os.mkdir(path)

    if model < 10 or model > 16:
        raise ValueError(f"Unacceptable iphone model: {model}")

    # 設定搜尋參數
    google_crawler = GoogleImageCrawler(
        feeder_threads=1,  # 提供圖片URL的線程數
        parser_threads=2,  # 解析HTML的線程數
        downloader_threads=4,  # 下載圖片的線程數
        storage={'root_dir': path}  # 儲存圖片的目錄
    )

    q = f'\"iphone {model}\" back -icon -cover'  # + "".join([f' -{str(i)}' for i in range(10, 16 + 1) if i != model])
    # print(q)

    # 搜尋的設定參數，這裡可以修改
    search_params = {
        'q': q,  # 搜尋關鍵字
        'max_num': amount,  # 最大下載圖片數量
        'file_idx_offset': 0,  # 起始圖片編號
        'filters': {
            'type': 'photo',  # 圖片類型: photo, clipart, lineart, face, animated
            'size': 'medium',  # 圖片大小: large, medium, icon 或 '>寬x高' 格式
            'color': 'color',  # 顏色選項: color, blackandwhite, transparent
        }
    }

    # 開始執行搜尋與下載
    google_crawler.crawl(
        keyword=search_params['q'],
        max_num=search_params['max_num'],
        file_idx_offset=search_params['file_idx_offset'],
        filters=search_params['filters'],
        overwrite=True
    )


"""
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO
"""

"""
def crawl(model: int, max_amount: int = 0):
    if model < 10 or model > 16:
        raise ValueError(f"Unacceptable iphone model: {model}")

    KEYWORD = f'\"iphone {model}\"'
    PATH: str = f'./dataset/iphone-{str(model)}'
    SCROLL_PAUSE_TIME = 2  # 滾動間隔
    MAX_IMAGES = max_amount if max_amount >= 0 else float("Inf")  # 下載的最大圖片數量
    INCLUDE_WORDS = [f"iphone {model}"]  # alt屬性中需要包含的字詞
    EXCLUDE_WORDS = [f' {str(i)} ' for i in range(10, 16 + 1) if i != model]  # alt屬性中排除的字詞

    # 初始化 Selenium
    driver = webdriver.Chrome()
    search_url = f"https://www.google.com/search?tbm=isch&tbs=isz:l"
    driver.get(search_url)

    # 搜尋圖片
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(KEYWORD)
    search_box.send_keys(Keys.RETURN)

    # 滾動頁面以載入更多圖片
    def scroll_to_bottom():
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    # scroll_to_bottom()
    driver.execute_script("window.scrollTo(0, 0);")

    # 下載圖片函數
    def download_image(url, file_path):
        try:
            response = requests.get(url, timeout=5)
            image = Image.open(BytesIO(response.content))
            image.save(file_path)
        except Exception as e:
            print(f"圖片下載失敗: {e}")

    # 選擇並下載圖片
    os.makedirs(PATH, exist_ok=True)
    images = driver.find_elements(By.CLASS_NAME, "YQ4gaf")
    image_count = 0

    for img in images:
        if image_count >= MAX_IMAGES:
            break

        alt_text = img.get_attribute("alt")
        if (any(word.lower() in alt_text for word in INCLUDE_WORDS) and
                not any(word.lower() in alt_text for word in EXCLUDE_WORDS)):
            try:
                img.click()
                time.sleep(1)  # 等待大圖加載

                img_url = img.get_attribute("src")

                if img_url and "http" in img_url:
                    file_name = f"{image_count + 1}.jpg"
                    file_path = os.path.join(PATH, file_name)
                    download_image(img_url, file_path)
                    print(f"下載圖片: {file_name}")
                    image_count += 1
            except Exception as e:
                print(f"圖片處理失敗: {e}")
        else:
            print(any(word.lower() in alt_text for word in INCLUDE_WORDS))
            print(any(word.lower() in alt_text for word in EXCLUDE_WORDS))
            print(alt_text)
            print(img.get_attribute("src"))
            print(img.get_attribute("alt"))
            time.sleep(60)
            break

    driver.quit()
    print(f"共下載 {image_count} 張圖片。")
"""

