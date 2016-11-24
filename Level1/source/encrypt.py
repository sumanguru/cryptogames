#Source code for weak encryption oracle in Lvl1 of cryptogames
#Shortly, implements a block cypher with 16-character blocks, 0 padding and fixed key
#In other words, *so very insecure*
#Compiled to an executable with pyinstaller
#By Tuomas Tinus aka sumanguru@github
#License: Public Domain, do whatever you wish but I'd appreciate being credited
#Contact me at tuomas.tinus@gmail.com (PGP key available on keyservers/keybase.io)

#!/usr/bin/python

text = input("Enter text to encrypt:")
key = bytearray('3EK/7:)5P^)NgGq0', 'utf8')
output = ''
null = ''

while ( len(text) > 0 ):
	
	if ( len(text) < 16 ):
		block = text.ljust( 16, '0' )
		text = ''
	else :
		block = text[0:16]
		text = text[16:len( text )]
	block = bytearray(block, 'utf8')
	for i in range(len(block)):
		block[i] = block[i]^key[i]
	block = str(bytes(block), 'utf-8')
	output = ''.join((output, block))

output = output.encode()
output = output.hex()
print(output)
