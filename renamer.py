import os
import argparse

parser = argparse.ArgumentParser(description="Renames files to numerical order.")
parser.add_argument('-path', dest='path', type=str, help='The path to the folder containing the files you want to rename')
parser.add_argument('-format', dest='format', type=str, help='The file format you want to rename the file to. (Note: Does not change the actual data of the file. Just the name.)')

args = parser.parse_args()

def main():
    path = args.path
    count = 1

    for root, dirs, files in os.walk(path):
        for i in files:
            os.rename(os.path.join(root, i), os.path.join(root, str(count) + '.' + args.format))
            count += 1


if __name__ == '__main__':
    main()
