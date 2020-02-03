# level 0
# http://www.pythonchallenge.com/pc/def/0.html
# http://www.pythonchallenge.com/pc/def/274877906944.html

print(2**38)

# level 1
# http://www.pythonchallenge.com/pc/def/map.html
# http://www.pythonchallenge.com/pcc/def/ocr.html
import string
text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
lmu ynnjw ml rfc spj."""

table = str.maketrans(
  string.ascii_lowercase,
  string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
print (str.translate(text,table) )

url = "http://www.pythonchallenge.com/pc/def/map.html"
print(url.translate(table))

# level 2
# http://www.pythonchallenge.com/pc/def/ocr.html
# http://www.pythonchallenge.com/pcc/def/equality.html


import urllib.request as ur
import re

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
response = ur.urlopen(url)
body = response.read()
page_source = re.search("<!--\n%(.|\s)+",body.decode()).group(0)

def count_char(mes):
    infos = {}
    for i in mes:
        if i.isalpha():
            if i not in infos:
                infos[i] = 0
            infos[i] += 1

    #a = sorted(infos.items(), key=lambda item: item[1])[0:10]
    a=''.join([c for c in infos if infos[c] < 2])
    print(a)


count_char(page_source)


# ´ð°¸2
import string
st=''
for ch in filter(lambda x: x in set(string.ascii_letters), page_source):
    st = st + ch
print(st )
