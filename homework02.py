import sys
import json

def read_csv(file_name):
    contents = []
    with open(file_name, 'r') as handle:
        for line in handle:
            if line.startswith("sample"):
                header = line.strip().split(',')
                print(header)
                continue
            splitted = line.strip().split(',')
            print(splitted)
            d = dict(zip(header,splitted))
            contents.append(d) 
    return contents

def to_json(l:list):
    with open("json_homework.json", 'w') as handle:
        json.dump(l, handle, indent = 4)

if __name__== "__main__":
    if len(sys.argv) != 2:
        print(f"Usage : python {sys.argv[0]}[json]")
        sys.exit()

    file_name = sys.argv[1]
    t = read_csv(file_name)
    f = to_json(t)
