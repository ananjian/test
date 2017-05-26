import re
#x = 'stephen.marquard@uct.ac.za'
#x= ' ashish lives in 0225 begen street *$#'
#y = re.findall('[0-9]',x)
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print y
