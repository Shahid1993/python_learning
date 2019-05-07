#https://askubuntu.com/questions/893019/monitor-folder-and-run-command-if-there-is-a-file-there
#!/usr/bin/env python3
import subprocess
import os
import time
import shutil

source = "/path/to/sourcedir"
target = "/path/to/targetedir"
files1 = os.listdir(source)

while True:
    time.sleep(2)
    files2 = os.listdir(source)
    # see if there are new files added
    new = [f for f in files2 if all([not f in files1, f.endswith(".sh")])]
    # if so:
    for f in new:
        # combine paths and file
        trg = os.path.join(target, f)
        # copy the file to target
        shutil.move(os.path.join(source, f), trg)
        # and run it
        subprocess.Popen(["/bin/bash", trg])
        print(trg)
    files1 = files2
