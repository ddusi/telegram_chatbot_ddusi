from flask import Flask, render_template, request
from decouple import config
import requests

app = Flask(__name__)

token=config("TELEGRAM_BOT_TOKEN")
chat_id=config('CHAT_ID')
url = "https://api.telegram.org/bot"

#webhook으로 설정한 url
@app.route(f'/{token}', methods=["POST"])
def telegram():
 # 챗봇에서 내가쓴 데이터 읽어오기
 re_data=request.get_json()

 # json데이터에서 원하는 정보뽑기
 re_id= re_data['message']['chat']['id']
 text=re_data['message']['text']

 # 챗봇에게 다시보내기
 requests.get(f'{url}{token}/sendmessage?chat_id={re_id}&text={text}')

 #200은 접속성공을 의미하는 숫자임!
 return "ok", 200   


if __name__ == ("__main__"):
 app.run(debug=True)