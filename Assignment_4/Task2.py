FILE_NAME="output.txt"
write=input("Enter text to write to the file: ")
with open(FILE_NAME,'w') as file:
    file.write(write+"\n")
print("Data successfully written to output.txt.")
print("\n")
additional=input("Enter additional text to append: ")
with open(FILE_NAME,'a') as file:
    file.write(additional+"\n")
print("Data successfully appended.")
print("\n")
print("Final content of output.txt:")
with open(FILE_NAME,'r') as file:
    final=file.read()
print(final)
