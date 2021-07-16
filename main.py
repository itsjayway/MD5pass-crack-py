from subprocess import call
import os

# main.py is intended to be run from the terminal
hashes = input("Word list file: ")                                                  # i.e.: rockyou.txt
while True:
    user_pass_file_dir = input("What is the name of the file you want to crack? ")  # i.e.: originalfile.txt
    # note: originalfile.txt is intended to contain lines with format username:password_hash
    content = []                                                                    # initialize empty array
    try:
        with open(user_pass_file_dir) as f:                                      # open originalfile.txt
            content = f.readlines()                                              # populate content arr with a line per index
        content = [x.strip() for x in content]
    except:
        print("Please enter a valid file directory")
    #file.close()                                                                   # close originalfile.txt (source file)

    output_file_name = "parsed_hashes.txt"                                          # indiciate filename of just hashes to look at
    new_file = open(output_file_name, "w")                                          # designate new_file as a to-write file with name parsed_hashes
    for line in content:                                                            # for each line stored in the indixes of content
        line_arr = line.split(":")                                                  # local variable line_arr set to [username, password_hash]
        new_file.write(line_arr[1]+"\n")                                            # write just the password_hash to parshed_hashes
    new_file.close()                                                                # close new_file.txt

    os.chdir("hashcat-6.2.2")                                                       # change file access to the hashcat directory
    print("\nHere's what was found...\n")
    pot_file = "outfile.txt"                                                        # hash : pass
    with open(pot_file, "w") as pot:                                                # open
        pot.truncate(0)                                                             # clear so not to overwrite
    call(["./hashcat.exe", "-m", "0", "../" + output_file_name, "../" + hashes, "-o", pot_file, "--potfile-disable"]) # call(...) is as if you're typing the arguments in the cmd line
    break

print("\nUsername%-*sPassword%s" % (20,"",""))      # "table" formatting
print("========================================")
out_content = []                                    # store outfile contents in out_content
with open("outfile.txt") as new_f:
    out_content = new_f.readlines()
out_content = [x.strip() for x in out_content]      # remove whitespace

i = 0
for line in content:
    lst = line.split(":")
    try:
        print("%-*s %s" %(20, lst[0], out_content[i].split(":")[1]))    # if out_content[i] exists, print the username and password
    except:
        print("%-*s %s" % (20, lst[0], "Not found in table"))           # otherwise print username and "Not found in table"
    i += 1
f.close()
new_f.close()