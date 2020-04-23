from urllib import parse
import requests
centers = [
 (32.766434, -117.081886),
 (32.7590688, -117.1618495),
 (32.733253, -117.054108),
 (32.623028, -117.070381),
]
for i,center in enumerate(centers):
    lon = center[1]
    lat = center[0]
    s = '''{"type":"features","features":[{"geometry":{"x":''' + str(lon) + ',"y":' + str(lat) + ''',"spatialReference":{"wkid":4326}}}],"doNotLocateOnRestrictedElements":true}'''
    url = "https://sampleserver3.arcgisonline.com/ArcGIS/rest/services/Network/USA/NAServer/Service%20Area/solveServiceArea?f=json&returnFacilities=false&returnBarriers=false&returnPolylineBarriers=false&mergeSimilarPolygonRanges=false&overlapLines=false&overlapPolygons=false&splitLinesAtBreaks=false&splitPolygonsAtBreaks=false&trimOuterPolygon=false&defaultBreaks=0.6213712%2C1.8641136&impedanceAttributeName=Length&restrictionAttributeNames=OneWay&travelMode=null&facilities=" + parse.quote(s)
    r = requests.get(url)
    with open("./arcgis_km/{0}.json".format(i+1), "w") as f:
        f.write(r.text)