#coding:utf-8

class YaGenerate (object):

    def __init__(self, fileexport):
        try:
            self.f_create = open(fileexport, 'w')
        except:
            raise IOError('Unable to create file, something whith user rights?')

    def header_add(self, TitleText):
        self.f_create.write('<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n')
        self.f_create.write('<title>'+TitleText+'</title>\n')
        self.f_create.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
        self.f_create.write('<script src="https://api-maps.yandex.ru/2.1/?lang=ru_RU" type="text/javascript"></script>\n'
                            '<script type="text/javascript">\n'
                            'ymaps.ready(init);\n')

    '''
    через запятую, переменные
    '''
    def autofillvar (self, mapvar, varibles):
        self.f_create.write('var '+mapvar+','+varibles+';\n')

    def map_placemark_add (self, map):
        pass

    def map_init(self, mapvar, idmap, center, zoom):
        self.f_create.write('function init()\n{' + mapvar + ' = new ymaps.Map("' + idmap + '", {center: [' + str(
            center) + '],zoom: ' + str(zoom) + '});\n')

    def add_places (self,mapvar, varible, coords, hintContent, balloonContent, markpath):
        self.f_create.write(str (varible)+" = new ymaps.Placemark(["+coords+"], {hintContent: '"+hintContent+"',balloonContent: '"+balloonContent+"'}, {iconLayout: 'default#image',iconImageHref: '"+markpath+"',iconImageSize: [30, 30],});"+mapvar+".geoObjects.add("+varible+");\n")


    def end_of_file (self,idmap, widht, height):
        self.f_create.write('}</script>\n</head>\n<body>\n<div id="'+idmap+'" style="width:'+str(widht)+'px; height: '+str(height)+'px">\n</div>\n</body>\n</html>')



    def save (self):
        self.f_create.flush()
        self.f_create.close()

#yapi = YaGenerate ('index.html')
#yapi.header_add('Апишки')
#yapi.autofillvar('mapa','placemark1,placemark2,placemark3,placemark4')
#yapi.map_init('mapa', 'map', '55.1173070102086, 36.6162455400635', 16)
#yapi.add_places('mapa', 'placemark1', '55.1173070102086, 36.6162455400635', 'Хер','Банулий хер')
#yapi.end_of_file('map', 800, 600)
#yapi.save()

'''
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Быстрый старт. Размещение интерактивной карты на странице</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <script src="https://api-maps.yandex.ru/2.1/?lang=tr_TR" type="text/javascript"></script>
    <script type="text/javascript">
        ymaps.ready(init);
        var myMap,
            myPlacemark;

        function init(){
            myMap = new ymaps.Map("map", {
                center: [55.1173070102086, 36.6162455400635],
                zoom: 7
            });

            myPlacemark = new ymaps.Placemark([55.1173070102086, 36.6162455400635 ], {
                hintContent: 'Москва!',
                balloonContent: 'Столица России'
            });

            myMap.geoObjects.add(myPlacemark);
        }
    </script>
</head>
<body>
    <div id="map" style="width: 600px; height: 400px"></div>
</body>
</html>
'''