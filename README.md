# FJU-Course-Insight
輔大師資課程智慧評鑒系統
## 一、專題簡介
FJU-Course-Insight 是一個專為輔大學生打造的課程評價分析平台。本專題旨在解決選課資訊不透明的問題，結合爬蟲技術與 AI 分析，讓學生能快速獲取各課程與授課老師的真實評價，作為選課決策依據。

## 二、專題目標
1. 建立 GitHub repository，完成版本控制與協作架構。
2. 建立 Flask 網站作為前後端服務核心。
3. 整合 PostgreSQL 資料庫，儲存爬取的評語資料。
4. 開發 Python 爬蟲模組，針對 Dcard/Threads 等平台收集相關資料。
5. 實作「資料預處理」與「AI 分類」模組，對評語進行情緒標記（如：涼課、嚴苛、認真）。
6. 將網站部署至 Render 雲端平台，實現公開服務。

## 三、系統架構
使用者瀏覽器
 -> Flask Web App
 -> PostgreSQL Database (儲存評語與分類結果)
 -> 資料分析與視覺化 Dashboard

## 四、資料庫設計
本專題使用 PostgreSQL 儲存資料：
* **comments_table**: 存放原始評語、老師名稱、課程名稱、AI 分類標籤、評價次數。

## 五、使用技術
* Python, Flask, PostgreSQL, Render
* BeautifulSoup4, Requests (爬蟲)
* Pandas (資料處理)
* OpenAI API / NLP 模型 (AI 評價分析)

## 六、執行方式
1. Clone 專案：`git clone [你的網址]`
2. 設定環境變數 (`.env`)：配置資料庫連線字串。
3. 執行爬蟲：`python crawler.py` (自動爬取並分類資料)
4. 啟動網站：`python app.py`
