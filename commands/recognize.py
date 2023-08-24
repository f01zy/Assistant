import config

from fuzzywuzzy import fuzz

def recognize(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in config.data['cmds'].items():
 
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC