import sys

def reducer():
    key=None
    current_value=0
    for line in sys.stdin:
        line=line.strip()
        line=line.split(",")
        current_key=line[0]
        if key == current_key:
            current_value+=int(line[1])
        else:
            if current_key:
                print(key,current_value,sep=", ")
                key=current_key
                current_value=0
    print(key,current_value,sep=", ")

reducer()
