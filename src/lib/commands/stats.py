# coding: utf8
import requests, json


def stats(args):
    api = 'API от osu!'
    user_id = args[0]
    r = requests.post('https://osu.ppy.sh/api/get_user', data={'k': api, 'u': user_id})
    user = json.loads(r.text)
    res = u'Статистика ' + user_id + u':  '+\
          u'Play Count: '+ user[0]['playcount']+ \
          u', PP: ' + user[0]['pp_raw'] + \
          u', Место в мире: ' + user[0]['pp_rank']+\
          u', Место по стране: '+user[0]['pp_country_rank'] +\
          u', lvl: '+user[0]['level']+\
          u', acc: ' + user[0]['accuracy'][:4]
    return res

