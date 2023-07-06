from scapy.all import * #used to craft and send ICMP packets and receive responses
from time import time, strftime #used to keep track of response time
import argparse #used to accept and parse the user's input IP address from the command line terminal

def traceroute(dest_ip, max_hops=30):
    ttl = 1 #initialize time to live at 1
    while True: 
        pkt = IP(dst=dest_ip, ttl=ttl) / ICMP()
        # Send the packet and get the reply
        start_time = time() 
        reply = sr1(pkt, verbose=0, timeout=2) #send ICMP packet, don't wait for more than 2 seconds for response
        rtt = round((time() - start_time) * 1000)  #round-trip time in ms
        if reply is None: #case where packet is lost or exceeds time limit
            print(f'{ttl}\t*\tRequest timed out.')
        elif reply.type == 0:  # type 0 is echo-reply which means we reached the destination
            print(f'{ttl}\t{reply.src}\t{rtt} ms\tDestination reached') #reached user inputted ip address print this fact
            break #stop the loop
        else:
            print(f'{ttl}\t{reply.src}\t{rtt} ms') #print hop number, IP address of hop, and round trip time
        ttl += 1 #increase time to live
        if ttl > max_hops: #break out of the infinite loop if we reach more than 30 hops
            print(f'Reached maximum hops count ({max_hops}). Exiting...')
            break

if __name__ == "__main__": #only run if directly executed by user
    parser = argparse.ArgumentParser(description='Python traceroute') #hold all info to parse command line arguments from terminal
    parser.add_argument('destination', metavar='D', type=str, help='Destination IP address') #to run this code, user needs to run the command python Project3.py <IP ADDRESS> **Note: sudo command may be necessary**
    args = parser.parse_args() #parse arguments return data
    print(f'Traceroute to {args.destination}:\nHop\tIP\t\tRTT') #tell the user we're running a tracerout to the IP address they specified
    traceroute(args.destination) #start the traceroute using converted user input 
