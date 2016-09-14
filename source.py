import itertools
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file", help="input file with chars/words")
parser.add_argument("-m", "--min", help="Minimum length of password")
parser.add_argument("-n", "--max", help="Maximium length of password")
parser.add_argument("-o", "--output", help="Filename to save to")

args = parser.parse_args()

content = [line.rstrip() for line in open(args.file)]
print(content)
raw_input("how does it look?")
countMax = 10000
count = 0
fileCount = 0
if args.output:
    f = open('passphrase' + str(fileCount), "w")
    for i in range(int(args.min), int(args.max)):
        res = itertools.product(content, repeat=i)
        for j in res:
            f.write(''.join(j) + "\n")
            count +=1
            if count > countMax:
                f.close()
                fileCount += 1
                f = open('passphrase' + str(fileCount), "w")
                count = 0
    f.close()
else:
    for i in range(int(args.min), int(args.max)):
        res = itertools.product(content, repeat=i)
        for j in res:
            print(''.join(j))

raw_input("Press any key to exit..")

