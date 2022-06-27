from ..cwxml.ymap import *

def import_ymap(import_op, filepath, import_settings):
    ymap_xml: CMapData = YMAP.from_xml_file(filepath)
    ymap_xml.write_xml("G:/Temp/!main/" + ymap_xml.name + ".ymap.xml")