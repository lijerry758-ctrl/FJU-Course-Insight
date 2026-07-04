# 功能註記：引入爬蟲所需套件
import requests
from bs4 import BeautifulSoup

def crawl_comments(keyword):
    # 功能註記：設定目標網址與請求標頭
    url = f"https://www.dcard.tw/search?query={keyword}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    # 功能註記：發送請求並獲取網頁資料
    response = requests.get(url, headers=headers)
    
    # 功能註記：解析 HTML 內容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 功能註記：顯示搜尋訊息
    print(f"正在搜尋：{keyword} 的資料...")
    return []

if __name__ == '__main__':
    # 功能註記：測試爬蟲功能
    crawl_comments("輔大課程")