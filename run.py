import os, platform

try:

    import requests
    from time import sleep
    from time import sleep as waktu


except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    print('W8 for next update')
    time.sleep(2)


elif bit == '32bit':

    print('W8 for next update')
