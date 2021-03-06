from http.client import HTTPSConnection
from http.client import HTTPException
from urllib.parse import quote
import simplejson


class Translator:

    def get_yandex_translate(self, searching_text, to_language):
        try:
            quoted_text = quote(u"" + searching_text + "")
            req = '/api/v1.5/tr.json/translate?' \
                  'key=trnsl.1.1.20150629T151613Z.82119cbb3415f490.ba44aa922a8b28e549144e0e2fa6249c7508358e' \
                  '&text=' + quoted_text \
                  + "&lang=" + to_language \
                  + '&options=1'

            conn = HTTPSConnection('translate.yandex.net')
            conn.request("GET", req)
            rez = conn.getresponse()
            data = rez.read()
            conn.close()

            if rez.status == 200:
                ddata = data.decode("utf-8")
                j = simplejson.loads(ddata, )
                tr_text = ''.join(j['text'])
                print(tr_text)
                return tr_text
            else:
                print("Something is wrong: " + str(rez.status) + " status code")
                print(data)

        except HTTPException as err:
            print(err)

    def determine_lang(self, txt):
        # TODO add more languages
        # TODO add more sophisticated determine methods
        is_rus = False
        char = hex(ord(txt[0]))
        for k in range(0x0400, 0x04FF + 1):
            if char == hex(k):
                is_rus = True
                break

        if is_rus:
            return "en"
        else:
            return "ru"
