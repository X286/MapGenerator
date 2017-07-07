#coding: utf-8
from Config import *
from DBExport import *
from MapPack import *

conf = get_config('conf/config')
conn = DBConn (conf.get('dbconn', 'dbname'), conf.get('dbconn', 'uname'),conf.get('dbconn', 'host'), conf.get('dbconn', 'port'), conf.get('dbconn', 'upassword'))
rows = conn.select("""SELECT id, model, napravlenie, name_camera, archive_server, program,
       install_place, owner_name, serial_num, date_install, date_deinstall,
       locations, descritption, is_ip_camera, is_bg_camera, picture_path,
       ST_AsText (geom), inventar_num, work_ability
       FROM cameras;""")
yapi = YaGenerate ('index.html')
yapi.header_add('Апишки')



strvar = ''
coords = []
files = []
cameradisc = []
for row in rows :
    strvar += 'place_'+str(row[17]).replace('-','')+','
    files.append('Pictures/'+str(row[17])+'.png')
    k = row[16].replace ('POINT(','').replace(')','')
    splitted = k.split (' ')
    coords.append(splitted[1]+','+splitted[0])
    cameradisc.append(str (row[12]))

yapi.autofillvar('mapa',strvar[:-1])
strwar  = strvar[:-1].split(',')

yapi.map_init('mapa', 'map', '55.1173070102086, 36.6162455400635', 16)
for k, var in enumerate(strwar):
    yapi.add_places('mapa', var, coords[k], 'Камера','<p>'+cameradisc[k]+'</p><img src ="'+files[k]+'" style = "width:300px; height:250px"/>', 'large.jpg')
yapi.end_of_file('map', conf.get('divproperties', 'width'), conf.get('divproperties', 'height'))
yapi.save()

conn.close()