import os

def readfile(input):
    output = []
    lines = 0
    name = os.path.basename(input)
    with open(input) as f:
        for line in f:
            output.append(line.strip())
            lines += 1
    return lines, name, output

def build(source_dir,source_files):
    files =[]
    for file in source_files:
        files.append(readfile(source_dir + file))
    files.sort()
    return files

def export(files,output_file):
    f = open(source_dir + output_file,'at')
    for file in files:
        f.write(file[1] + '\n')
        f.write(str(file[0]) + '\n')
        for string in file[2]:
            f.write(string + '\n')
    f.close()

source_dir = '/home/alex/Python/python/Hello World/Files/Folder/'
source_files = ['1.txt','2.txt','3.txt']
output_file = '4.txt'
files = build(source_dir,source_files)
export(files,output_file)





