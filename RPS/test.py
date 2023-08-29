import subprocess
import select
import re
import requests as req

bot_token="6418283142:AAEXtK_MkMaa8_8_ZVxhHIZ1CQlb_P7SXAM"
group_id="-1001914228287"

def send_message(content):
    endpoint = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': group_id, 'text': content}
    data = req.post(endpoint, data=payload)

def get_message(text):
    pattern = r'\[\*\*] \[(\d+/\d+-\d+:\d+:\d+\.\d+)\] (.*?) {.*?} (\d+\.\d+\.\d+\.\d+:\d+) -> (\d+\.\d+\.\d+\.\d+:\d+)'
    matches = re.findall(pattern, text)

    for match in matches:
        timestamp, message, source_ip, dest_ip = match
        out = f"Timestamp: {timestamp}, Pesan: {message}, Source IP: {source_ip}, Dest IP: {dest_ip}"
        send_message(out)


def show_live_output(proc):
    while True:
        ready, _, _ = select.select([proc.stdout], [], [], 1)  # Menunggu hingga output tersedia
        if proc.stdout in ready:
            line = proc.stdout.readline()
            if not line:
                break
            get_message(line)

            #print(line.decode('utf-8').strip())

# Ganti 'perintah_anda' dengan perintah yang ingin Anda jalankan
perintah = ['sudo', 'snort', '-i', 'ens33', '-c', '/etc/snort/snort.conf', '-l', '/var/log/snort/', '-A', 'console', '-K', 'ascii']

# Membuka proses dan mengarahkan outputnya
proses = subprocess.Popen(perintah, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

# Memanggil fungsi untuk menampilkan output secara live
show_live_output(proses)

# Menunggu proses selesai
proses.wait()