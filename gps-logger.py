# coding: utf-8

from functions import *
import serial
import os

while True:
    s = object

    try:
        # GPS モジュールに接続する
        s = serial.Serial(str_device, int_rate, timeout=int_timeout)

        flg_start = False
        int_error_count = 0
        dict_gps_lines = {}
        while True:
            try:
                # GPS 信号を取得する
                list_buffer_line = s.readline().split('\n')
                list_gps_line = list_buffer_line[0].split(',')

                if flg_start is False and list_gps_line[0] == str_gga:
                    # 最初の GGA 行から処理を開始する
                    flg_start = True

                if flg_start is True:
                    # 受信した GPS 信号を辞書に保存する
                    dict_gps_lines.update({list_gps_line[0]: list_gps_line})

                    if list_gps_line[0] == str_zda:
                        # ZDA 行でデータを区切る
                        # 扱いやすいデータに変換する
                        dict_gps_data = {
                            'latitude': to_dd(
                                dict_gps_lines[str_gga][3], to_float(dict_gps_lines[str_gga][2])),
                            'longitude': to_dd(
                                dict_gps_lines[str_gga][5], to_float(dict_gps_lines[str_gga][4])),
                            'condition': to_int(dict_gps_lines[str_gga][6]),
                            'satellites': to_int(dict_gps_lines[str_gga][7]),
                            'level': to_float(dict_gps_lines[str_gga][8]),
                            'antenna_height': to_float(dict_gps_lines[str_gga][9]),
                            'geoid_height': to_float(dict_gps_lines[str_gga][11]),
                            'datetime': utc_to_gmt_0900(
                                dict_gps_lines[str_rmc][9], dict_gps_lines[str_rmc][1]
                            ).strftime(str_datetime_format)
                        }

                        # 変換したデータを出力する
                        message(dict_gps_data)
                        str_filename = dict_gps_lines[str_rmc][9] + dict_gps_lines[str_rmc][1]
                        if not os.path.exists(path_converted_data):
                            os.makedirs(path_converted_data)
                        with open(path_converted_data + '/' + str_filename, 'a') as f:
                            f.write(str(dict_gps_data))

                        # 辞書を空にする
                        dict_gps_lines = {}
                        dict_gps_data = {}

                int_error_count = 0

            except Exception as e:
                message(error_gps_data_receive)
                message(e)
                flg_start = False

                # 一定回数エラーが続いたら GPS の再接続を行う
                int_error_count += 1
                if int_error_count >= int_threshold:
                    raise Exception(error_gps_data_receive_over_threshold)

    except Exception as e:
        message(error_gps_connection)
        message(e)

    # GPS モジュールとの接続を初期化する
    del s






