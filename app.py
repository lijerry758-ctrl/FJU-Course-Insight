# 導入 Flask 框架，這是建立網頁的核心工具
from flask import Flask, render_template

# 初始化 Flask 應用程式
app = Flask(__name__)

# 設定網頁首頁的路由 (網址路徑)
@app.route('/')
def index():
    # 回傳首頁的 HTML 畫面 (稍後建立)
    return "輔大課程評鑑系統準備中！"

# 程式入口點，當執行此腳本時啟動伺服器
if __name__ == '__main__':
    app.run(debug=True)