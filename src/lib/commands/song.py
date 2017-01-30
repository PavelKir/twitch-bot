# coding: utf8
import vk
from urllib import quote

def song(args):
    type = args[0]
    if (type=='osu' or not type):
        f = open('E:/OSU/Files/np_playing.txt')
        return f.read()
    elif (type=='vk'):
        session = vk.AuthSession(app_id='ID ПРИЛОЖЕНИЯ ВК', user_login='ЛОГИН ОТ ВК', user_password='ПАРОЛЬ ОТ ВК', scope='status')
        vkapi = vk.API(session)
        status = vkapi.status.get(user_id=19258377)

        if ('audio' in status):
            songname = status['audio']['artist'] + ' - ' + status['audio']['title']
            url = 'https://vk.com/search?c[q]='+ quote(songname.encode('cp1251')) +'&c[section]=audio'
            return songname + ', ' + url.replace(' ','+').replace('[','%5B').replace(']','%5D')
        else:
            return u'В данный момент я не слушаю музыку в вк..'