# Google Chrome Dark Mode Enabler for Linux

It has been 3 years since Google Chrome on Linux has this bug: Enabling dark mode on your system won't affect Chrome's UI. That's something easily fixable, but the Google team decided to completely ignore this issue for years. It is known that you can fix this yourself by creating a conf file, but it is a manual process and sometimes you just wanna change the theme without doing that. With this in mind, I decided to create these two Python scripts that'll do all the work for you. It's not a definitive fix, but it is certainly better than using nano and pasting the flags all the time.

1. Open the terminal and type: 
``` git clone https://github.com/Mutcholoko/Chrome-Linux-DarkMode.git ```

2. Type: ``` cd Chrome-Linux-DarkMode ```

3.1. If you want to enable Dark Mode, type on terminal: 
``` sudo python chrome_dark.py ``` (it'll ask you for your password)

3.2. If you want to go back to Light Mode, type on terminal: 
``` sudo python chrome_light.py ``` (it'll also ask you for your password)


And that's pretty much it. This is a really simple script, nothing much special about it. I was thinking about creating an UI to run this, but I decided it was not worth the time. Feel free to do so if you think it'll be useful!
