import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/keime/デスクトップ/lisner-talker/install/my_pkg'
