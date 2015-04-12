import sys
input_file= open(sys.argv[1]).readlines()
input_file= [ i.split('\r\n')[0].strip(',') for i in input_file]
for i in input_file:
    print i
outputfile= open(sys.argv[1]+'_output','w')
for i in input_file:
    outputfile.write(i+'\n')