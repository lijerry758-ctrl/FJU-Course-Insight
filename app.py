# 這是主程式入口，負責啟動網頁服務
from flask import Flask, render_template

# 初始化 Flask 應用程式
app = Flask(__name__)

# 設定首頁路由，目前先讓它回傳一個簡單的歡迎字串
@app.route('/')
def index():
    return "輔大師資課程智慧評鑒系統開發中！"

# 執行程式的啟動設定
if __name__ == '__main__':
    app.run(debug=True)