import sys
import os

# Default Metadata
metadata = {"font" : "Noto Sans Thai", "size" : "12"}

def get_input_path():
    if not sys.argv[1]:
        print("[ Error ] Input not specified")
        exit(2)
    if not os.path.exist(sys.argv[1]):
        print("[ Error ] Input specified does not exist")
        exit(2)
    return sys.argv[1]

# Data for parse()
hierarchy = []
order = 0

def parse(buff):
    # Metadata: overwrite the default value
    if buff.startswith("+"):
        colon_pos = buff.find(":")
        key = buff[1:colon_pos].strip()
        val = buff[colon_pos+1:].strip()
        metadata[key] = val
        return

    # Remove any leading space
    pre_strip = len(buff)
    buff = buff.lstrip("\t")
    
    # Count leading tab
    dept = pre_strip - len(buff)

    # If the line is a comment: do nothing
    if buff.startswith("--"):
        return
    # If the line is a modifier
    if buff.startswith("%"):
        pass # TODO
    # TODO parse regular node line

def main():
    input_path = get_input_path()

    with open(input_path) as f:
        for line in f:
            parse(line)
