import os

username = os.environ.get('SUDO_USER', os.environ.get('USERNAME'))

fp = os.path.join("/home/" + username + "/.var/app/com.google.Chrome/config/", "chrome-flags.conf")
if not os.path.isfile(fp):
    print("Chrome is not in dark mode")
    exit(1)

os.remove(fp)