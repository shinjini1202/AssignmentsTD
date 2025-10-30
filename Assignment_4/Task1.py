import os
FILE_NAME="sample.txt"
if os.path.exists(FILE_NAME):
    print("Reading file content:")
    with open(FILE_NAME,'r') as file:
        line_num=0
        for line in file:
            line_number+=1
            print(f"Line {line_num}:{line.strip()}")
else:
    print("File does not exist")
