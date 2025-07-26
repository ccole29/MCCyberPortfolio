from scapy.all import *
import os

def wifi_scanner(interface="wlan0"):
    os.system(f"ifconfig {interface} down")
    os.system(f"iwconfig {interface} mode monitor")
    os.system(f"ifconfig {interface} up")

    def packet_handler(pkt):
        if pkt.haslayer(Dot11Beacon):
            ssid = pkt[Dot11Elt].info.decode()
            mac = pkt[Dot11].addr2
            print(f"Network SSID: {ssid}, MAC: {mac}")

    sniff(iface=interface, prn=packet_handler)

wifi_scanner()
