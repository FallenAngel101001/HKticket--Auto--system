from seleniumbase import SB
import Action
import random

'''
proxy = [ HERE IS YOUR proxt --> xxx.xxx.xxx.xxx@port]
a = random.choice(proxy)
'''

with SB(undetected=True) as sb:
    # here to put your link of HKTICKET
    sb.open("https://premier.hkticketing.com/shows/show.aspx?sh=LEGEN0923")
    sb.Action(sb)
    sb.sleep(100)
