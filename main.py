from subprocess import call
import os

hashes = input("Word list file: ")
while True:
    user_pass_file_dir = input("What is the name of the file you want to crack? ")
    content = []
    try:
        with open(user_pass_file_dir) as file:
            content = file.readlines()

    except:
        print("Please enter a valid file directory")

    new_file = open("parsed_hashes", "w")
    for line in content:
        line_arr = line.split(":")
        new_file.write(line_arr[1]+"\n")
    # call(["cd", "hashcat-6.2.2"])
    os.chdir("hashcat-6.2.2")
    call(["./hashcat.exe", "-m", "0", "../" + user_pass_file_dir, "../" + hashes, "--show"])
    # print("\nParse successful")
    break