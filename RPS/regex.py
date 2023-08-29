import re

text = "08/28-01:10:59.633088  [**] [1:3:0] Terdapat Indikasi Serangan DDoS [**] [Priority: 0] {TCP} 172.100.43.253:8475 -> 172.100.43.251:80"

def get_message(text):
    pattern = r'\[\*\*] \[(\d+/\d+-\d+:\d+:\d+\.\d+)\] (.*?) {.*?} (\d+\.\d+\.\d+\.\d+:\d+) -> (\d+\.\d+\.\d+\.\d+:\d+)'
    matches = re.findall(pattern, text)

    for match in matches:
        timestamp, message, source_ip, dest_ip = match
        out = f"Timestamp: {timestamp}, Pesan: {message}, Source IP: {source_ip}, Dest IP: {dest_ip}"
        print(out)

get_message(text)
