import os, platform

try:

    import requests,time,sleep

except:

    os.system('pip install requests')
    os.system('git pull')
    os.system(' pip uninstall requests chardet urllib3 idna certifi -y ')
    os.system('pip install chardet urllib3 idna certifi requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    print('W8 for next update')
    time.sleep(1000)


elif bit == '32bit':

    print('W8 for next update')
    time.sleep(1000)
