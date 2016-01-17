import requests
from urllib.parse import urlparse
import json
import urllib
import random
from time import gmtime, strftime


sendMsgUrl = "http://d1.web2.qq.com/channel/send_buddy_msg2"



cookies = {
    'pgv_pvi': '7557615616',
    'RK': '3CPWQ0dsOT',
    'ptcz': 'af181601973d54d924f56bdb6f6b52b54bee6eb6955d5ab748f42443e1238729',
    'ts_refer': 'www.google.com.tw/',
    'ts_uid': '3239985255',
    'pgv_info': 'ssid=s314675712',
    'pgv_pvid': '995119604',
    'o_cookie': '280974109',
    'pt_clientip': 'c9250a821c586b4d',
    'pt_serverip': 'f3100a8f826148bb',
    'pt2gguin': 'o0280974109',
    'uin': 'o0280974109',
    'skey': '@ABXOWZoq5',
    'p_uin': 'o0280974109',
    'p_skey': '1B9mJNpEUR5RsyzeRKfHmD9-2segQHY4FEDIDWh-JoY_',
    'pt4_token': 'qoEM5A6E8SzbGsq0tYI*oB-3h2LbaicjHUrHtkyalis_',
    'ptwebqq': 'a5f30f22945bb6fbaadd6fd96184e7f3a6a8f9392f22aef8a829366f1e87789c',
}

headers = {
    'Origin': 'http://d1.web2.qq.com',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Referer': 'http://d1.web2.qq.com/proxy.html?v=20151105001&callback=1&id=2',
    'Connection': 'keep-alive',
}

# contentStr = str(123)
# requestData = {  
#    "to":3825116274,
#    "content":"[\"" + contentStr +"\",[\"font\",{\"name\":\"Algerian\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]",
#    "face":351,
#    "clientid":53999199,
#    "msg_id":62340005,
#    "psessionid":"8368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857"
# }

# dataStr = urllib.parse.quote(json.dumps(requestData))
# dataStr = "r=" + dataStr.replace("%20", "")


def sendMsg(content_str, dst_id, msg_id):
	requestData = {  
	   "to":dst_id,
	   "content":"[\"" + content_str +"\",[\"font\",{\"name\":\"Algerian\",\"size\":10,\"style\":[0,0,0],\"color\":\"000000\"}]]",
	   "face":351,
	   "clientid":53999199,
	   "msg_id":62340005,
	   "psessionid":"8368046764001d636f6e6e7365727665725f77656271714031302e3133332e34312e383400001ad00000066b026e040015808a206d0000000a406172314338344a69526d0000002859185d94e66218548d1ecb1a12513c86126b3afb97a3c2955b1070324790733ddb059ab166de6857"
	}

	dataStr = urllib.parse.quote(json.dumps(requestData))
	dataStr = "r=" + dataStr.replace("%20", "")
	r = requests.post(sendMsgUrl, headers = headers,  cookies = cookies, data = dataStr)	
	print(r.text)

def main():
	for x in range(1,10):
		content_msg = "roll 了：" + str(random.randrange(1,10)) +" \n&& \n" + strftime("%Y-%m-%d %H:%M:%S", gmtime())
		sendMsg(content_msg , 3825116274, 62340005)

if __name__ == '__main__':
	main()