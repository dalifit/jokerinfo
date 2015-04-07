import urllib, os
import binascii

#jokerinfo
#dalifit
#hackfest

n=0
data=''
f = open('dalifit.zip','w')
while (n<324):
	response = urllib.urlopen('http://www.ctf.tn/tasks/prog/crawler/checkme/'+str(n))
	html = response.read()
	if not html:
       		break
	print html
	data=data+html
	n+=1
f.write(binascii.a2b_hex(data))
f.close()
