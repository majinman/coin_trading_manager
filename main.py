#-*- coding:utf-8 -*-

import sys
sys.path.append("..")


from flask import Flask, abort, g
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import flash
from flask import send_file
from database import db
from config import getConfig
import utils
import arrow
from model.coin_info import CoinInfo
from model.stoploss import Stoploss
from model.price_notification import PriceNotification
from model.candle import Candle
from model.account import Account
from model.portfolio import Portfolio
from api.stoploss import stoploss_blueprint
from api.notification import notification_blueprint
from api.monitor import monitor_blueprint
from api.upbit import upbit_blueprint
from api.candle import candle_blueprint
from api.order import order_blueprint
from api.account import account_blueprint
from crawler.coin import update_coin_info

from service.monitor_manager import monitor_manager


app = Flask(__name__, template_folder='templates')
app.config.from_object(getConfig())
app.jinja_env.lstrip_blocks = True
app.jinja_env.trim_blocks = True

app.register_blueprint(order_blueprint, url_prefix='/order')
app.register_blueprint(stoploss_blueprint, url_prefix='/stoploss')
app.register_blueprint(notification_blueprint, url_prefix='/notification')
app.register_blueprint(monitor_blueprint, url_prefix='/monitor')
app.register_blueprint(upbit_blueprint, url_prefix='/upbit')
app.register_blueprint(candle_blueprint, url_prefix='/candle')
app.register_blueprint(account_blueprint, url_prefix='/account')


with app.app_context():
    print("###### Initializing Server ######")
    db.init_app(app)
    db.create_all(app=app)
    update_coin_info()
    app.monitor = None
    print("####### Done initializing Server ######")



@app.route('/')
def home():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, threaded=True)
