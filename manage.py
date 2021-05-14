#-*- coding:utf-8 -*-
import sys
sys.path.append("..")

from flask_script import Manager
from flask_script import Command, Manager, Option
from main import app
from config import getConfig
import arrow
from service.monitor_service import monitor_service
from service.upbit_service import upbit_service
from service.candle_service import candle_service, CandleService, get_rebound
from service.order_service import order_service
from service.balancing_service import balancing_service
from service.portfolio_service import portfolio_service
from model.candle import Candle
from model.coin_info import CoinInfo
from sqlalchemy import or_


from database import db

import sys
sys.path.append("..")
manager = Manager(app)


@manager.command
def monitor():
    monitor_service.run()
    sys.exit()

@manager.command
def get_candle_day():
    all_coin = db.session.query(CoinInfo).filter(CoinInfo.market.startswith("KRW")).all()

    for coin in all_coin:
        upbit_service.get_candle(coin.market, upbit_service.DAYS, 10, 30)

    sys.exit()

@manager.option('-u', '--unit', help='What unit?')
def get_candle_min(unit):
    """
        -command ex) python manage.py get_candle_min -u 240

    """
    all_coin = db.session.query(CoinInfo).filter(or_(CoinInfo.deleted==False, CoinInfo.deleted==None)).filter(CoinInfo.market.startswith("KRW")).all()

    for coin in all_coin:
        upbit_service.get_candle(coin.market, Candle.MINUTES, 10, unit)

    sys.exit()

@manager.command
def clear_stoploss():
    order_service.clear_stoploss()
    sys.exit()

@manager.command
def settle():
    balancing_service.settle_account()
    sys.exit()

@manager.command
def candle():
    candle_service.get_direction("KRW-ATOM", Candle.MINUTES, 15, 300, 120)


@manager.command
def rebound():
    get_rebound()

@manager.command
def update_portfolio():
    portfolio_service.update_portfolio()
    sys.exit()


@manager.command
def get_orderbook():
    """
        호가정보 받아오기
    :return:
    """
    print(upbit_service.get_orderbook(['KRW-GAS', 'KRW-BTC']))


@manager.command
def test():
    market = 'KRW-DAWN'
    candles = db.session.query(Candle).filter(Candle.market==market).filter(Candle.period=='d').order_by(Candle.date.desc()).limit(30).all()
    candle_service = CandleService()
    candle_service.set_candles(candles)
    candle_service.set_market(market)
    candle_service.find_bullish_candle()
    candle_service.is_approach_open(market=market)




if __name__ == "__main__":
    manager.run()