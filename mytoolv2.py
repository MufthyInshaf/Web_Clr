#color code
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))

def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

#tool name
prGreen("+---------------------------------------------------------+")
prGreen('         |  | _ \  |      __|  |     _ \ ')
prGreen('         |  |   /  |     (     |       /    ')
prGreen('         \__/ _|_\ ____| \___| ____| _|_\ ')                                                 
prRed(" v.02                                      Dev : Mufthy.I")
prGreen("+--------------------------------------------------------+")
#url getting
import time
import urllib.request
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen(input('enter domin url :> '))
print( )
#result code
x = "result code: " + str(webUrl.getcode())
#weburl code
data = webUrl.read()
#password gen
import random
s = "abcdefghijkl\
       mnopqrstuvwxyz1234\
       567890ABCDEFGHIJKLM\
       NOPQRSTUVWXTZ!@$%^&*\
       ( )_-+[ ]{ };/'; . ,"
passwordlen = 16
password = " " . join(random.sample(s,passwordlen))
#select items
a = prCyan("[1] Active test ")
n = prCyan("[2] Open url code")
z = prCyan("[3] Malicious link generator")
s = prYellow("[4] Strong password generator")
q = prYellow("[5] IG crash") 
print()
#select option num
d = input ("enter option num: ")
#test ip
import socket
hostname = socket.gethostname( )
IPADDr = socket.gethostbyname(hostname)
prYellow("[*] Test ip : " + IPADDr)
print( )
# see result code 
if d == "1" :
	time.sleep(3)
	prPurple(x)
	prRed(" !!!working!!!")
#see weburl code	
if d == "2":
	prPurple(x)
	time.sleep(1)
	print("Openlink")
	time.sleep(1)
	print("Reading source code")
	print( )
	time.sleep(1)
	print("* ")
	time.sleep(1)
	print(" * * ")
	time.sleep(1)
	print("* * * ")
	time.sleep(1)
	print(" * * * * ")
	time.sleep(1)
	print("* * * * * ")
	time.sleep(1)
	print(" * * * * * * ")
	time.sleep(1)
	print("* * * * * * * ")
	time.sleep(1)
	print(" * * * * * * * * ")
	time.sleep(1)
	print("* * * * * * * * * ")
	time.sleep(1)
	print(" * * * * * * * * * * ")
	print("")
	print("")
	prGreen(data)
#Malicious
q = 'https://bit.ly/3pRoI7h'
if d == "3" :
	time.sleep(1)
	prYellow("[*] running Malicious link server")
	prYellow("[*] Connecting server")
	
	print(". ")
	time.sleep(1)
	print(". .")
	time.sleep(1)
	print(". . . ")
	time.sleep(1)
	print(". . . . ")
	time.sleep(1)
	print(". . . . . ")
	time.sleep(1)
	print(". . . . . . ")
	time.sleep(1)
	print(". . . . . . .")
	time.sleep(1)
	print(". . . . . . . . ")
	time.sleep(1)
	print(". . . . . . . . .")
	time.sleep(1)
	print(". . . . . . . . . . ")
	time.sleep(3)
	print("Running Succsessfull")
	time.sleep(5)
	prYellow("[*] starting Malicious generator")
	time.sleep(6)
	print( )
	prPurple("        Malicious link = https://bit.ly/3pRoI7h ")
	print( )
	prRed("(WARNING : Dont click in your device.This is a very harmful link)")
if d == "4" :
	time.sleep(3)
	print("your password = ", password)
if d == "5" :
	time.sleep(1)
	print("copy and past victim account,")
	print( )
	prGreen("✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘ ✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘ ✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘ ✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢⇣͢✘͢͢⁦ ✘͢͢ۦོ͢✘͢͢ۦོ͢⇣͢✰͢↬ÂмRØ^^O̷ ꦿ⃕O̷↬ۦོ͢✰͢...")


'''print()
print("Enter option number:>")
input()
count = 1
while (count<=2):
    print(j)
    count += 1'''

print( )
input( )