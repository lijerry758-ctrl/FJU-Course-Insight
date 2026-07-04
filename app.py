# 功能註記：引入 Flask 框架與網頁渲染功能
from flask import Flask, render_template

# 功能註記：初始化 Flask 應用程式
app = Flask(__name__)

# 功能註記：設定首頁路徑，並指向 index.html
@app.route('/')
def index():
    return render_template('index.html')

# 功能註記：執行 Flask 伺服器
if __name__ == '__main__':
    app.run(debug=True)
