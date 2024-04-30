#!/usr/bin/env python3
# this script written by zwerd

import sys

def hex_to_ascii(hex_string):
    hex_values = hex_string.split('%')[1:]
    try:
        ascii_string = ''.join([chr(int(val, 16)) for val in hex_values])
        return ascii_string
    except ValueError:
        return "Invalid hex values provided"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <hex_string>")
        sys.exit(1)
    
    hex_string = sys.argv[1]

    # Convert hex string to ASCII
    ascii_string = hex_to_ascii(hex_string)

    # Print the ASCII string
    print(ascii_string)
