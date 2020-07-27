import sys
import json

def read_txt(file_name:str):
    contents = ""
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                continue
            contents += line.strip()
    return contents

def read_csv(file_name :str):
    contents = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(',')
                continue
            splitted = line.strip().split(',')
            d = dict(zip(header,splitted))
            contents.append(d)
    return contents

def read_tsv(file_name):
    contents = []
    with open(file_name, 'r') as handle: 
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header,splitted))
        content.append(d)
    return contents

def to_json(l, file_name):
    with open("sample_json", 'w') as handle:
        json.dump(l,handle, indent = 4)

if __name__== "__main__":
    if len(sys.argv) != 2:
        print(f" Usage: Python {sys.argv[0]}[csv]")
        sys.exit()

    file_name = sys.argv[1]
    
