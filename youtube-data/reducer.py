import sys

def reducer():
    current_key=None
    current_value=0
    key=None

    for line in sys.stdin:
        line=line.strip()
        line=line.split(",")
        current_key=line[0]
        if current_key == key:
            current_value+=int(line[1])
        else:
            if current_key:
                print(key,current_value,sep=",")
                key=current_key
                current_value=int(line[1])

    print(key,current_value,sep=",")



reducer()
