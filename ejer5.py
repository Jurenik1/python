

#sacar ejecutables

import os

x=os.lisdir("C:\Windows\System32")
	for z in x:
	if z[-3:]=="exe":
		print z