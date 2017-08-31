'''Make fasta file with various headers compatible with Trinotate
This is done by inserting "TRINITY_DN[number]_c0_g1_il" in directly 
after the caret symbol followed by a pipe to separate and not lose all original
information.
'''

import sys, re, os

fasta = sys.argv[1]

fastaFile = open(sys.argv[1])

first, ext = os.path.splitext(fasta)

newName = first+"_renamed.fasta"

newFasta = open(newName, 'w')

regex = r">(.*)\n"

nextLine = 1

for line in fastaFile:
    if line.startswith('>'):
        atter = re.search(regex, line)
        attergroups = atter.groups()
        trinName = ">TRINITY_DN"+str(nextLine)+"_c0_g1_i1 | "+attergroups[0]+"\n"
        newFasta.write(trinName)
        nextLine += 1
    else:
        newFasta.write(line)