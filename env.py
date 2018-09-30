# coding: utf-8

# デバッグモードが True のときはエラーメッセージを出力する
flg_debug = False

# GPS モジュールの制御に使う情報
str_device = '/dev/ttyS0'
int_rate = 9600
int_timeout = 5
int_threshold = 3
str_datetime_format = '%Y/%m/%d %H:%M:%S'

# NMEA フォーマットの操作に使う情報
str_gga = '$GPGGA'
str_rmc = '$GPRMC'
str_zda = '$GPZDA'

# GPS 情報の保存先ディレクトリ
path_converted_data = '/home/pi/python-gps-logger/data'

# Google Drive API の接続情報
path_key_file = '/home/pi/GPS Logger-5dd765bb82f5.json'
url_gcp_api_oauth_scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]
str_spreadsheet_name = 'GPS Logger'

# PostgreSQL にデータを保存するパターンも検討する予定
db_host = '127.0.0.1'
db_port = 5432
db_user = 'gps_logger'
db_pass = 'gps_logger'
db_name = 'gps_logger'

