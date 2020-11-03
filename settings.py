import os

current_dir = os.path.dirname(os.path.realpath(__file__))

# Database
#database = "amazon_crawler"
#host = ""
#user = ""

# Redis
#redis_host = ""
#redis_port = 6379
#redis_db = 0

# Request
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "en-US,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
}
allowed_params = ["node", "rh", "page"]

# Proxies
proxies = ['175.139.179.65:42580',
 '171.97.15.12:8080',
 '149.255.154.62:8080',
 '181.48.47.26:53281',
 '85.187.17.39:53281',
 '113.254.178.224:8383',
 '123.56.75.226:3128',
 '165.16.25.62:9999',
 '212.83.170.121:3838',
 '41.72.203.182:42928',
 '80.245.117.131:8080',
 '212.126.107.2:31475',
 '194.152.235.171:8080',
 '101.255.125.124:8080',
 '59.153.17.186:53281',
 '203.202.245.58:80',
 '54.228.137.107:80',
 '77.94.144.162:3128',
 '200.105.157.218:53281',
 '103.78.213.226:45163',
 '176.56.107.95:43930',
 '170.82.73.33:9999',
 '31.28.99.25:31396',
 '41.79.35.1:8080',
 '197.255.253.210:58136',
 '110.74.208.154:21776',
 '192.109.165.83:80',
 '179.26.221.225:8080',
 '49.248.32.110:48434',
 '197.211.238.220:54675',
 '46.161.232.236:8080',
 '51.75.147.41:3128',
 '200.38.19.236:80',
 '103.81.114.182:53281',
 '190.112.136.177:8085',
 '138.59.150.198:8080',
 '51.132.217.104:3128',
 '200.35.56.161:35945',
 '167.61.129.43:8080',
 '114.57.49.242:53281',
 '46.29.9.46:38430',
 '103.86.187.244:8080',
 '146.59.226.253:3128',
 '103.251.176.22:32108',
 '177.250.168.36:8080',
 '197.221.89.70:8080',
 '179.52.99.184:999',
 '123.27.3.246:39915',
 '46.101.124.192:3128',
 '203.223.34.2:8080',
 '85.117.61.186:49929',
 '200.69.79.218:55443',
 '149.54.10.226:8080',
 '181.176.185.83:999',
 '82.137.244.151:8080',
 '105.27.238.165:80',
 '93.185.96.61:43749',
 '198.50.163.192:3129',
 '41.191.205.121:8888',
 '190.54.100.74:8080',
 '192.41.13.71:3128',
 '128.199.202.122:8080',
 '14.192.31.4:50838',
 '203.192.199.114:8080',
 '83.171.114.92:45822',
 '178.128.91.99:8080',
 '177.74.128.234:3128',
 '118.174.233.40:42106',
 '182.23.54.146:58519',
 '201.234.60.10:999',
 '134.35.206.191:8080',
 '177.250.238.229:8080',
 '103.217.173.210:53905',
 '79.115.245.227:8080',
 '169.239.182.151:3128',
 '190.80.11.32:8080',
 '212.83.178.20:3838',
 '67.225.164.154:80',
 '196.214.145.106:80',
 '190.186.1.46:55830',
 '139.255.25.83:3128',
 '200.77.147.78:32392',
 '103.227.255.43:80',
 '180.211.183.178:60604',
 '191.96.42.80:8080',
 '170.0.54.248:8080',
 '78.46.173.189:8080',
 '62.176.1.194:35608',
 '36.89.183.241:49044',
 '200.116.232.66:3128',
 '154.72.204.122:8080',
 '45.248.139.140:8080',
 '89.32.227.190:8080',
 '52.149.152.236:80',
 '109.127.82.3:9090',
 '188.240.114.188:8080',
 '190.148.208.57:999',
 '189.204.242.178:8080',
 '5.189.133.231:80',
 '46.99.131.27:51671',
 '1.255.48.197:8080',
 '89.218.5.109:37717',
 '201.204.168.106:63141',
 '195.154.56.105:3838',
 '191.5.0.79:53281',
 '183.88.194.85:8080',
 '117.69.231.91:30001',
 '168.228.51.197:59144',
 '41.32.229.249:80',
 '88.255.102.106:8080',
 '208.163.39.218:53281',
 '47.52.231.140:8080',
 '193.110.115.220:3128',
 '200.87.43.26:999',
 '213.230.127.139:3128',
 '51.15.153.117:3838',
 '197.221.85.214:8080',
 '181.78.12.51:9992',
 '124.40.250.246:3128',
 '154.127.38.65:60020',
 '202.142.159.26:48970',
 '180.242.19.131:3128',
 '190.61.49.243:999',
 '64.137.176.32:3128',
 '138.68.161.14:3128',
 '170.244.68.106:8080',
 '168.0.86.146:8080',
 '165.16.25.18:9999',
 '167.172.109.12:38463',
 '45.7.238.58:8080',
 '160.0.218.25:8080',
 '136.244.107.87:3128',
 '118.99.104.6:8080',
 '185.37.211.222:50330',
 '201.204.46.10:39371',
 '1.179.183.73:50178',
 '185.186.81.155:999',
 '190.57.143.66:50719',
 '113.130.126.2:31932',
 '116.212.129.58:59557',
 '132.145.18.53:80',
 '190.152.12.54:41031',
 '85.113.14.42:8080',
 '190.120.248.8:999',
 '79.125.163.225:30677',
 '93.91.196.242:9090',
 '186.225.157.22:8080',
 '196.2.14.250:45521',
 '103.1.93.184:55443',
 '175.141.69.200:80',
 '113.254.178.224:8197',
 '158.255.57.174:51172',
 '185.121.2.31:8080',
 '202.75.111.74:47009',
 '139.5.71.46:23500',
 '212.73.68.156:3128',
 '88.198.24.108:8080',
 '200.85.169.18:47548',
 '202.51.68.14:59175',
 '103.254.167.74:34327',
 '82.137.244.74:8080',
 '192.119.110.78:3128',
 '91.142.12.34:8081',
 '115.84.99.182:51265',
 '52.69.19.32:80',
 '36.67.246.50:41202',
 '190.2.210.139:8080',
 '83.171.98.129:44380',
 '203.81.91.80:8080',
 '82.200.233.4:3128',
 '192.109.165.28:80',
 '41.77.81.90:8080',
 '213.160.187.139:53281',
 '78.60.203.75:47385',
 '106.104.170.66:8080',
 '102.176.160.75:41701',
 '153.142.70.170:8080',
 '208.80.28.208:8080',
 '85.30.198.53:55443',
 '190.122.186.232:8080',
 '109.75.47.248:59010',
 '175.100.103.170:55443',
 '104.128.228.69:8118',
 '79.106.45.54:8080',
 '36.89.187.193:43032',
 '160.119.128.102:21213',
 '195.24.53.195:8080',
 '178.136.2.208:55443',
 '185.10.68.103:80',
 '200.71.104.30:8888',
 '159.203.61.169:3128',
 '95.179.143.201:3128',
 '103.98.79.225:53284',
 '179.26.236.121:8080',
 '51.81.82.175:80',
 '178.79.24.36:8080',
 '78.47.16.54:80',
 '41.223.143.78:3128',
 '154.73.85.37:43388',
 '191.101.39.124:80',
 '186.195.90.16:8080',
 '51.79.158.45:3128',
 '51.75.147.43:3128',
 '189.113.217.35:49733',
 '188.166.83.17:3128',
 '197.155.83.17:8080',
 '174.130.50.208:8080',
 '190.171.168.90:999',
 '170.238.255.90:31113',
 '95.9.194.13:56726',
 '95.68.115.202:53281',
 '203.81.95.42:8080',
 '47.52.228.127:80',
 '95.168.96.42:34273',
 '103.57.70.231:39143',
 '116.197.129.242:37822',
 '46.239.40.185:8080',
 '119.206.242.196:80',
 '61.29.96.146:8000',
 '77.221.52.77:33694',
 '190.53.38.98:46340',
 '45.70.106.55:55443',
 '154.64.219.15:8888',
 '121.230.54.122:9999',
 '62.210.147.54:3838',
 '90.189.116.152:3128',
 '170.254.224.7:55443',
 '182.23.54.211:54525',
 '115.75.1.156:38351',
 '190.53.46.2:44612',
 '89.221.223.234:80',
 '134.209.29.120:3128',
 '178.135.51.30:8080',
 '134.35.131.231:8080',
 '103.83.37.138:3838',
 '35.204.30.79:3128',
 '190.120.250.53:999',
 '51.79.142.230:38414',
 '27.116.51.119:8080',
 '103.216.82.44:8080',
 '212.156.149.38:53100',
 '91.126.239.175:8080',
 '154.127.38.129:60020',
 '46.20.59.243:58658',
 '190.211.241.148:8081',
 '103.56.235.186:443',
 '84.214.150.146:8080',
 '113.185.19.134:8080',
 '195.62.70.252:8080',
 '103.148.79.106:8080',
 '103.115.164.65:8080',
 '195.230.115.115:8080',
 '188.166.251.91:8080',
 '118.174.234.11:33208',
 '83.150.10.212:80',
 '216.250.236.11:3128',
 '212.83.167.87:3838',
 '91.214.128.243:23500',
 '140.227.229.208:3128',
 '80.48.119.28:8080',
 '105.27.238.162:80',
 '41.79.150.226:8080',
 '113.252.222.73:80',
 '89.144.19.91:3128',
 '109.75.42.231:53597',
 '37.111.42.210:8080',
 '213.230.121.113:3128',
 '103.225.221.139:80',
 '178.134.208.126:50824',
 '41.216.233.186:8080',
 '89.248.244.182:8080',
 '77.70.35.87:37475',
 '207.154.231.213:8080',
 '188.166.213.220:8118',
 '196.0.111.194:34638',
 '203.202.245.62:80',
 '113.161.207.105:60626',
 '178.134.152.146:8080',
 '103.146.177.39:80',
 '149.5.37.113:8080',
 '154.72.202.62:53281',
 '139.162.193.152:80',
 '45.231.221.1:999',
 '119.206.242.196:8380',
 '139.162.78.109:8080',
 '49.48.91.62:8080',
 '193.239.56.196:45673',
 '80.87.185.233:8080',
 '41.60.216.175:8080',
 '181.211.11.3:8080',
 '160.2.59.45:8080',
 '103.193.138.193:8080',
 '103.105.195.2:3128',
 '212.179.18.73:3128',
 '135.181.91.172:7733',
 '217.64.109.231:45282',
 '83.96.237.121:80',
 '185.189.199.75:23500',
 '81.183.198.239:8080',
 '186.219.96.47:54570',
 '178.128.109.50:8118',
 '134.35.55.31:8080',
 '168.138.209.186:8000',
 '31.40.135.67:31113',
 '162.243.108.129:8080',
 '92.86.10.42:42658',
 '178.252.80.226:34730',
 '194.143.248.186:8080',
 '190.2.212.19:999',
 '43.225.67.35:53905',
 '143.255.143.178:8080',
 '36.66.61.119:8080',
 '89.218.5.110:37717',
 '41.65.146.38:8080',
 '105.234.154.230:55472',
 '113.53.91.12:53281',
 '41.220.114.154:8080',
 '182.71.157.206:80',
 '190.184.144.170:58975',
 '45.82.245.34:3128',
 '188.166.213.185:8118',
 '188.166.238.58:8118',
 '122.254.83.161:8080',
 '36.67.143.183:58387',
 '200.38.19.229:80',
 '185.15.108.37:8080',
 '128.199.224.56:8118',
 '81.174.11.227:47324',
 '210.103.3.169:8080',
 '62.87.151.132:38615',
 '185.52.8.81:32219',
 '5.234.160.221:8080',
 '152.0.249.39:8080',
 '157.245.108.35:80',
 '186.251.225.228:3128',
 '200.85.173.186:8080',
 '213.6.204.153:49044',
 '41.65.174.91:8080',
 '36.94.33.62:45620',
 '80.233.134.119:3128',
 '105.27.238.161:80',
 '195.154.242.205:3838',
 '37.120.192.154:8080',
 '105.234.155.230:8080',
 '95.217.102.133:3128',
 '45.230.176.146:23500',
 '213.197.148.230:8090',
 '182.71.157.205:80',
 '201.217.245.229:49160',
 '169.255.75.117:34403',
 '198.199.86.11:8080',
 '67.219.113.93:8080',
 '46.246.12.3:3128',
 '59.153.87.242:8080',
 '188.156.240.240:8118',
 '165.255.88.166:8888',
 '156.222.205.232:8080',
 '122.15.131.65:57873',
 '186.150.193.30:999',
 '41.188.5.110:8080',
 '94.130.179.24:8041',
 '118.175.93.148:36744',
 '161.202.226.194:8123',
 '103.250.156.22:30093',
 '119.82.249.4:60959',
 '163.172.113.179:3838',
 '135.181.36.161:8888',
 '190.216.147.70:41310',
 '125.62.213.18:84',
 '175.140.47.196:8080',
 '95.216.155.54:3128',
 '36.91.68.150:8080',
 '191.101.39.91:80',
 '178.143.12.2:8080',
 '114.6.88.238:60811',
 '201.249.61.60:8080',
 '160.202.146.198:8080',
 '91.234.127.222:53281',
 '188.166.229.243:8118',
 '138.68.240.218:3128',
 '45.229.87.161:999',
 '196.250.176.77:33486',
 '103.14.36.218:8080',
 '161.35.70.249:8080',
 '36.72.125.199:8080',
 '167.179.4.142:55443',
 '194.135.75.74:55716',
 '88.82.95.146:3128',
 '212.98.190.22:3128',
 '95.216.214.160:3128',
 '173.212.202.65:80',
 '202.166.207.195:8080',
 '195.1.208.121:80',
 '216.250.236.10:3128',
 '197.159.70.200:8080',
 '151.232.72.22:80',
 '47.74.84.218:80',
 '213.105.29.14:3128',
 '102.129.249.120:8080',
 '135.181.82.183:3128',
 '213.230.69.33:8080',
 '81.161.61.88:35953',
 '103.53.45.74:8080',
 '121.211.254.46:8080',
 '197.159.23.174:39150',
 '193.95.228.13:53281',
 '121.123.61.231:8080',
 '188.166.139.135:4905',
 '41.72.196.49:8080',
 '158.181.157.83:8080',
 '103.212.93.225:34184',
 '122.176.65.143:31021',
 '198.199.120.102:8080',
 '192.109.165.179:80',
 '176.9.75.42:8080',
 '176.123.27.31:8080',
 '91.193.253.188:23500',
 '83.174.203.222:59015',
 '46.238.48.82:8080',
 '84.22.61.46:53281',
 '137.59.120.58:8080',
 '51.75.147.44:3128',
 '31.179.224.42:44438',
 '81.140.102.191:32231',
 '182.75.168.78:80',
 '103.125.130.30:8080',
 '217.195.203.28:3128',
 '169.239.223.136:39721',
 '138.197.157.32:8080',
 '1.20.97.181:55285',
 '182.52.90.42:51657',
 '196.27.107.216:8080',
 '190.12.95.170:47029',
 '182.191.84.39:80',
 '138.68.41.90:3128',
 '182.160.117.130:53281',
 '115.77.191.180:53281',
 '139.99.102.114:80',
 '190.152.0.130:55870',
 '85.114.112.174:80',
 '124.107.185.3:8080',
 '178.219.175.128:59064',
 '115.178.103.227:55443',
 '139.5.132.245:8080',
 '185.23.131.10:8080',
 '41.254.46.104:1973',
 '193.84.28.131:8080',
 '94.130.179.24:8009',
 '139.99.105.5:80',
 '51.15.158.28:3838',
 '59.127.27.243:8080',
 '182.253.169.168:8080',
 '88.248.23.216:36426',
 '213.230.127.137:3128',
 '182.71.157.203:80',
 '197.248.7.229:8080',
 '180.200.238.130:8080',
 '107.150.22.210:8080',
 '189.170.79.21:8080',
 '41.160.40.2:37741',
 '128.199.35.212:80',
 '212.116.65.244:55693',
 '5.11.17.105:1990',
 '183.88.71.246:8080',
 '102.176.160.70:61279',
 '178.252.166.210:8080',
 '64.4.94.129:80',
 '72.252.4.49:8080',
 '14.143.168.230:8080',
 '41.32.181.61:8080',
 '178.172.208.4:32231',
 '64.137.175.85:3128',
 '41.86.251.62:8080',
 '213.178.38.246:38978',
 '196.27.106.112:8080',
 '144.217.101.245:3129',
 '36.92.180.240:80',
 '134.209.200.146:8080',
 '61.118.35.94:55725',
 '176.9.119.170:8080',
 '150.145.110.91:80',
 '143.255.40.106:37620',
 '46.243.35.86:8080',
 '105.27.238.164:80',
 '202.92.4.150:1234',
 '27.255.58.6:8080',
 '35.235.115.241:80',
 '220.247.174.12:45954',
 '41.94.87.242:8080',
 '178.128.125.16:35793',
 '185.64.18.25:8080',
 '192.109.165.194:80',
 '181.225.213.227:999',
 '159.192.97.80:43278',
 '103.250.166.16:48340',
 '85.114.96.154:38081',
 '94.130.179.24:8011',
 '78.111.97.181:3141',
 '119.82.253.86:8080',
 '181.115.168.99:53281',
 '202.166.211.48:30753',
 '79.106.44.86:8080',
 '196.40.117.114:8080',
 '222.252.156.61:62694',
 '212.92.204.54:8080',
 '193.149.225.181:80',
 '200.68.62.10:8080',
 '195.62.70.254:8080',
 '154.0.155.205:8080',
 '103.224.185.48:32341',
 '196.0.34.142:33855',
 '140.238.84.65:3128',
 '128.199.135.209:8118',
 '180.247.138.59:3128',
 '41.221.106.50:8080',
 '77.28.97.34:48458',
 '41.220.131.55:8080',
 '180.250.101.146:8080',
 '103.89.159.5:8080',
 '41.87.73.182:8080',
 '1.20.102.102:38816',
 '195.178.33.86:8080',
 '186.248.170.83:53281',
 '115.243.35.98:8080',
 '210.63.206.156:80',
 '45.4.85.73:999',
 '180.250.12.10:80',
 '85.62.10.82:8080',
 '195.154.232.38:3838',
 '78.47.130.42:8080',
 '168.181.62.74:31732',
 '94.205.254.82:3128',
 '212.179.18.74:3128',
 '181.48.111.246:49094',
 '190.53.46.14:38525',
 '43.225.192.241:50878',
 '96.9.69.164:53281',
 '36.89.122.240:49784',
 '182.253.115.66:57733',
 '31.176.162.138:8080',
 '103.92.212.65:43399',
 '212.98.159.196:8080',
 '185.44.231.2:34244',
 '36.66.61.7:56232',
 '5.42.224.18:8080',
 '190.248.154.2:9992',
 '95.141.36.112:8686',
 '41.220.138.235:8080',
 '103.250.68.10:8080',
 '5.153.234.92:3128',
 '13.92.119.142:80',
 '150.129.151.42:6666',
 '43.242.242.196:8080',
 '5.20.91.12:60792',
 '181.176.161.39:999',
 '31.14.49.1:8080',
 '103.83.116.106:55443',
 '178.115.244.26:8080',
 '144.217.243.76:5566',
 '185.155.96.158:8080',
 '124.158.88.56:54555',
 '186.159.8.218:58122',
 '176.62.178.247:47556',
 '192.117.146.110:80',
 '105.27.238.163:80',
 '154.127.161.28:8080',
 '185.107.50.1:1234',
 '62.113.2.18:8080',
 '103.106.148.209:30223',
 '81.12.119.166:8080',
 '103.69.125.151:80',
 '83.69.93.64:44331',
 '185.114.137.14:32171',
 '85.62.10.84:8080',
 '175.100.5.52:32721',
 '190.149.165.162:51489',
 '124.219.176.139:39589',
 '141.105.174.47:80',
 '122.55.250.90:8080',
 '192.41.19.53:3128',
 '90.109.85.199:8080',
 '62.210.129.156:3838',
 '182.160.124.26:8081',
 '181.114.224.177:8080',
 '51.222.68.105:8080',
 '169.239.120.178:3128',
 '103.215.177.231:80',
 '163.172.108.37:80',
 '190.217.1.53:32192',
 '186.148.42.93:999',
 '168.90.110.178:999',
 '209.91.216.168:8080',
 '188.168.56.82:55443',
 '195.9.114.222:80',
 '128.199.108.222:8118',
 '90.157.198.182:8080',
 '51.15.123.85:3128',
 '20.54.136.125:80',
 '142.44.148.56:8080',
 '178.125.120.200:8080',
 '62.210.99.221:3838',
 '51.132.53.3:3128',
 '213.6.136.150:8080',
 '113.53.83.212:44664',
 '166.210.64.246:8080',
 '186.1.195.134:3128',
 '139.162.13.79:80',
 '45.224.23.193:999',
 '196.3.97.34:23500']

proxy_user = ""
proxy_pass = ""
proxy_port = ""

# Crawling Logic
start_file = os.path.join(current_dir, "start-urls.txt")
max_requests = 2 * 10**6  # two million
max_details_per_listing = 9999

# Threads
max_threads = 30

# Logging & Storage
log_stdout = True
image_dir = "/tmp/crawl_images"
export_dir = "/tmp"
