import xml.etree.ElementTree as ET
from iptools import IpRange

#CloudFlare IP Range List
#https://www.cloudflare.com/ips-v4
cloudflare_list = [
'199.27.128.0/21',
'173.245.48.0/20',
'103.21.244.0/22',
'103.22.200.0/22',
'103.31.4.0/22',
'141.101.64.0/18',
'108.162.192.0/18',
'190.93.240.0/20',
'188.114.96.0/20',
'197.234.240.0/22',
'198.41.128.0/17',
'162.158.0.0/15',
'104.16.0.0/12']
ips = []
#Parse dump.xml RosComNadzor
tree = ET.parse('dump.xml')
root = tree.getroot()
#Block Site List

for child in root:
   for ip_item in cloudflare_list:
        if child.find('ip').text in IpRange(ip_item):
            print(child.find('ip').text)
            ips.append(child.find('ip').text)
            print(['CloudFlare DNS: '+ ip_item,child.attrib['id'],child.find('domain').text,child.find('ip').text])
print('IP Адреса: ',list(set(ips)))
print('IP Адресов CloudFlare: ',len(list(set(ips))) )