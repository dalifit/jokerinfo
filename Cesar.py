import mechanize
#Jokerinfo
#dalifit
#hackfest
def decrypt(message,key):
	key = -key
	translated = ''
	for symbol in message:
		if symbol.isalpha():
			num = ord(symbol)
			num += key
			if symbol.isupper():
				if num > ord('Z'):
					num -= 26
				elif num < ord('A'):
					num += 26
			elif symbol.islower():
				if num > ord('z'):
					num -= 26
				elif num < ord('a'):
					num += 26
			translated += chr(num)
		else:
			translated += symbol
	return translated


br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)

br.set_handle_robots(False) 
response = br.open('http://www.ctf.tn/tasks/prog/prog1.php')
l= response.read()
k=l.split()

j=k[5].split('<br>')
print "cipher : "+j[0]+" key : "+k[6]
print decrypt(j[0],int(k[6]))
data = br.open('http://www.ctf.tn/tasks/prog/check1.php?p='+decrypt(j[0],int(k[6])))
print data.read()
