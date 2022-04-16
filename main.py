from subprocess import call
import os
import sys

def get_file_to_crack():
    hashes = os.path.abspath('rockyou.txt')
    if not os.path.isfile(hashes):
        hashes = input("Word list file: ")
    else:
        print(f'rockyou.txt found at {hashes}\n')
    
    return hashes

def print_ls():
    curr_dir = os.listdir()
    for f in curr_dir:
        print(f)

def read_db_hashes(filename):
    content = []
    while True:
        try:
            with open(filename) as f:
                content = f.readlines()
            content = [x.strip() for x in content]
            break
        except:
            print("Please enter a valid file directory")

def send_to_hashcat(output_file_name, hashes):
    os.chdir("hashcat-6.2.2")
    print("\nHere's what was found...\n")
    pot_file = "outfile.txt"
    with open(pot_file, "w") as pot:
        pot.truncate(0)
    call(["./hashcat.exe", "-m", "0", "../" + output_file_name,
            "../" + hashes, "-o", pot_file, "--potfile-disable"])

def parse_cracked():
    out_content = []
    with open("outfile.txt") as new_f:
        out_content = new_f.readlines()
    out_content = [x.strip() for x in out_content]

    hash = []
    for line in out_content:
        hash.append(line.split(":"))
    
    return hash

def print_formatted(content):
    print("%-*s %s" % (20, lst[0], content))
def main():
    hashes = get_file_to_crack()
    while True:
        print_ls()

        user_pass_file_dir = input(
            "\nWhat is the name of the file you want to crack? ")

        content = read_db_hashes(user_pass_file_dir)

        output_file_name = "parsed_hashes.txt"
        with open(output_file_name, 'w') as new_file:
            for line in content:
                line_arr = line.split(":")
                new_file.write(line_arr[1]+"\n")

        send_to_hashcat(output_file_name, hashes)
        break

    print("\nUsername%-*sPassword%s" % (20, "", ""))
    print("========================================")
    
    hash = parse_cracked()

    for value in content:
        lst = value.split(":")
        if lst[1] in hash:
            print_formatted(hash[hash.index(lst[1])+1])
        else:
            print_formatted("Not found in table")



if __name__ == '__main__':
    main()
