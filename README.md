# MD5pass-crack-py
Created for TheForage/Goldman Sachs Engineering Virtual Program

# Tutorial
- In addition to cloning this repo, you must also have: 
1) the [hashcat-6.2.2](https://hashcat.net/hashcat/) folder (download the "hashcat binaries" download)
2) [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

both in the same directory as main.py

# To run:
- Open a terminal in the directory of main.py (either right-click 'Git Bash Here' or 'dir'/'cd' yourself to it)
- python main.py
- enter filenames as:
-    rockyou.txt
-    originalfile.txt

Note: parsed_hashes.txt will be written to the same directory, this is an output containing a list of all the hashes in the [input file](originalfile.txt).


