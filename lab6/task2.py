import os

#1
def list_contents(path="."):
   
    all_items = os.listdir(path)
    
    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]
    
    print(f"Directories in '{path}': {directories}")
    print(f"Files in '{path}': {files}")
    print(f"All contents in '{path}': {all_items}")

#user_path1 = input("Enter the directory path: ")
#list_contents(user_path1)

#2
def check_path_access(path):
    
    print(f"Checking access for: {path}\n")
    
    if os.path.exists(path):
        print("Path exists.")
    else:
        print("Path does NOT exist.")
        return

    if os.access(path, os.R_OK):
        print("Readable.")
    else:
        print("Not readable.")

    if os.access(path, os.W_OK):
        print("Writable.")
    else:
        print("Not writable.")

    if os.access(path, os.X_OK):
        print("Executable.")
    else:
        print("Not executable.")

#user_path2 = input("Enter a path to check: ")
#check_path_access(user_path2)

#3
def check_path_info(path):
    
    if os.path.exists(path):
        print(f"The path exists: {path}")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"File name: {os.path.basename(path)}")
    else:
        print("The path does NOT exist.")

#user_path3 = input("Enter a path to check: ")
#check_path_info(user_path3)

#4
def count_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return sum(1 for line in file)

#file_path1 = input("Enter the file path: ")
#print("Number of lines:", count_lines(file_path1))

#5
def write_list_to_file(filename, data_list):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data_list:
            file.write(f"{item}\n")

file_path2 = input("Enter the file path: ")
data = []

print("Enter list items (type 'done' to finish):")
while True:
    item = input()
    if item.lower() == "done":
        break
    data.append(item)

#write_list_to_file(file_path2, data)
#print("List has been written to", file_path2)

#6
import string

def generate_text_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"This is file {filename}\n")

#generate_text_files()
#print("26 text files (A.txt to Z.txt) have been created.")

#7
def copy_file(source, destination):
    with open(source, 'r', encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dest:
        dest.write(src.read())

source_file = input("Enter the source file path: ")
destination_file = input("Enter the destination file path: ")

#copy_file(source_file, destination_file)
#print("File copied successfully.")

#8
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' has been deleted.")
        else:
            print("No write permission to delete the file.")
    else:
        print("The file does not exist.")

#file_path3 = input("Enter the file path to delete: ")
#delete_file(file_path3)