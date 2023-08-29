import re

text = """
08/29-15:08:34.145467  [**] [1:2005:1] Terjadi Indikasi Serangan Bruteforce SSH [**] [Priority: 0] {TCP} 172.100.43.253:42088 -> 172.100.43.251:22
08/29-11:50:09.673898  [**] [1:3:0] Terdapat Indikasi Serangan DDoS [**] [Priority: 0] {TCP} 172.100.43.253:53041 -> 172.100.43.251:80
"""

pattern = r"(\d{2}/\d{2}-\d{2}:\d{2}:\d{2}\.\d+)  \[.*\] \[(\d+:\d+:\d+)\] (.+) \[.*\] \[.*\] {(TCP|UDP)} (\d+\.\d+\.\d+\.\d+:\d+) -> (\d+\.\d+\.\d+\.\d+:\d+)"

matches = re.findall(pattern, text)

for match in matches:
    timestamp, rule_id, attack_desc, protocol, source_ip, dest_ip = match
    print(f"Timestamp: {timestamp} \nAttack Description: {attack_desc} \nProtocol: {protocol} \nSource IP: {source_ip} \nDestination IP: {dest_ip}")
    print()
