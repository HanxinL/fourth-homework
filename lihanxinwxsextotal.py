Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import itchat
█
>>> itchat.login()
Getting uuid of QR code.
Downloading QR code.
Please scan the QR code to log in.
Please press confirm on your phone.
Loading the contact, this may take a little while.
Login successfully as Diablo
>>> friends = itchat.get_friends(update = True )[0:]
male=
>>> male=female = other =0
>>> for i in friends[1:]:
	sex = i["Sex"]
	if sex ==1:
		male +=1
	elif sex ==2:
		female += 1
	else:
		other +=1
total = len(friends[1:])
SyntaxError: invalid syntax
>>> for i in friends[1:]:
	sex = i["Sex"]
	if sex ==1:
		male +=1
	elif sex ==2:
		female += 1
	else:
		other +=1

		
>>> total =len(friends[1:])
>>> print("男性好友：%.2f%%" % (float(male) / total * 100))
男性好友：60.00%
>>> print("女性好友：%.2f%%" % (float(female) / total * 100))
女性好友：31.87%
>>> print("其他：%.2f%%" % (float(other) / total * 100))
其他：8.12%
>>> LOG OUT!
