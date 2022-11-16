import os

username = os.environ.get('SUDO_USER', os.environ.get('USERNAME'))

fp = os.path.join("/home/" + username + "/.var/app/com.google.Chrome/config/", "chrome-flags.conf")
if not os.path.exists("/home/" + username + "/.var/app/com.google.Chrome/config/"):
    print("Error: You don't have Google Chrome installed")
    exit(1)

f = open(fp, "w")

l1 = "--force-dark-mode"
l2 = "--enable-features=WebUIDarkMode"

f.write(l1)
f.write("\n")
f.write(l2)
f.close()