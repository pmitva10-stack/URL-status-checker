import requests
urls=["https://google.com","https://wikipedia.com"
    ,"https://youtube.com","https://github.com"
    ,"https://chatgp.com","https://microsoft.com"]
#headers ={"Uer-Agent": "Mozilla/5.0"}#it sends the bunch of
#metadata alongside the requests. whereas user agent pretends to be
#a regular browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
for link in urls:
    try:
       response = requests.get(link,headers=headers)
       print(link,"is up",response.status_code)
    except:
        print(link," is unreachable")       