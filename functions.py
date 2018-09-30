# coding: utf-8

from env import *
from error import *
import datetime


# デバッグモードのときだけエラーメッセージを出力する
def message(subject):
    # デバッグモードのときだけ
    if flg_debug == 1:
        print(str(subject))
    return


# 変換元データを float に変換する
# 変換できない場合は 0.0 を返す
def to_float(val):
    try:
        float_val = float(val)
    except Exception as e:
        message(e)
        float_val = 0.0
    return float_val


# 変換元データを int に変換する
# 変換できない場合は 0 を返す
def to_int(val):
    try:
        int_val = int(val)
    except Exception as e:
        message(e)
        int_val = 0
    return int_val


# UTC 時間を日本時間に変換する
def utc_to_gmt_0900(str_date, str_time):
    str_year = '20' + str_date[4:6]
    str_month = str_date[2:4]
    str_day = str_date[0:2]

    str_hh = str(int(str_time[0:2]) + 9)
    str_mm = str_time[2:4]
    str_ss = str_time[4:6]

    timestamp = datetime.datetime.strptime(
        str_year + '/' + str_month + '/' + str_day + ' ' +
        str_hh + ':' + str_mm + ':' + str_ss
        , str_datetime_format
    ) + datetime.timedelta(hours=9)

    return timestamp


# 緯度経度を 00時00分000秒 の形式に変換する
def to_dd(str_azimuth, float_val):
    dd = float_val / 100
    mm = (((float_val / 100) - dd) * 100) / 60
    ss = (((((float_val / 100) - dd) * 100) - mm) * 60) / (60 * 60)

    float_val = dd + mm + ss

    # 南緯、西経を負にする
    if str_azimuth == 'S' or str_azimuth == 'W':
        float_val = float_val * -1

    return float_val

