from os import listdir
from os.path import isfile, join, isdir

if __name__ == "__main__":

    onlyfiles = [f for f in listdir("./") if isfile(join("./", f))]
    onlydirs = [f for f in listdir("./") if isdir(join("./", f))]

    print(onlyfiles)
    print(onlydirs)