from flask import Flask
import random
app = Flask(__name__)

dizi=["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
      "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
      "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
      "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor."]

@app.route("/rastgele_gercek")
def hello_world():
    return f'<h1>{random.choice(dizi)}</h1>\
    <a href="/">Ana Sayfaya Geri Dön</a>'


@app.route("/")
def rastgele():
    return '<a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a>' 

@app.route("/gizli-mekan")
def gizli():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <img src="/static/dedektif.png" alt="dedektif">
    </body>
    </html>
    '''

app.run(debug=True)