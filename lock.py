import os, sys

print ("\033[1;32mMasukan UserName&Password:)")
print ("\033[1;31;1mKalo Gak Tau Pm m3d 0813-5339-8031")
username = 'memed'      
password = 'Tamvan'

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

def main():
    uname = raw_input("username : ")
    if uname == username:
	pwd = raw_input("password : ")

	if pwd == password:
	    print "\n\033[1;34mHello Welcome user", 
	    sys.exit()

	else:
	    print "\n\033[1;36mMaaf password salah!!!\033[00m"
	    print "Login lagi\n"
	    restart()

    else:
	print "\n\033[1;36mMaaf username salah !!!\033[00m"
	print "Login lagi\n"
	restart()

try:
    main()
except KeyboardInterrupt:
    os.system('clear')
    restart()