# Snort_TelegramBot
Its Open-Source Script


# First Install Snort
You Can goto https://www.unixmen.com/install-snort-nids-ubuntu-15-04/
OR
1. Step one sudo apt-get update
2. sudo apt-get install snort -y

# Prepare Script
1. get UserID telegram
2. get Token Telegram

use https://api.telegram.org/bot+token/getUpdates to GetUserID
get Token From Bot Father
  
# Download Script
1. wget https://raw.githubusercontent.com/zailbreck/Snort_TelegramBot/master/bot_tele.sh --output-document=bot.sh
2. chmod 777 bot.sh

# How To Use
1. in New Terminal Enter snort -i [interface] -c /etc/snort/snort.conf -l /var/log/snort -A console > /home/snort/log.txt
2. in New Terminal Enter ./bot.sh
