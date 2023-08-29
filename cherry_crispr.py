import os
import Bio
import numpy as np
import pandas as pd
import argparse
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Blast.Applications import NcbiblastnCommandline


parser = argparse.ArgumentParser(description="""Main script of PhaSUIT.""")
parser.add_argument('--bfolder', help='Folder of the bacterial contigs',  default = 'NONE')
parser.add_argument('--ident', help='ident threshold for the alignment',  default = 75)
parser.add_argument('--threads', help='number of threads to use', type=int, default=8)
parser.add_argument('--rootpth', help='rootpth of the user', default='user_0/')
parser.add_argument('--out', help='output path of the user', default='out/')
parser.add_argument('--midfolder', help='mid folder for intermidiate files', default='dataset/')
parser.add_argument('--dbdir', help='database directory',  default = 'dataset/')
inputs = parser.parse_args()



threads   = inputs.threads
bfolder   = inputs.bfolder
rootpth   = inputs.rootpth
out       = inputs.out
dbdir     = inputs.dbdir
midfolder = inputs.midfolder
value     = float(inputs.ident)

if not os.path.exists(rootpth):
    os.system(f'mkdir {rootpth}')
    os.system(f'mkdir {rootpth}/{out}')
    os.system(f'mkdir {rootpth}/{midfolder}')


######################################################
#################  folder file  ######################
######################################################
elif bfile == 'NONE':
    os.system(f'mkdir {rootpth}/{midfolder}/crispr_tmp')
    os.system(f'mkdir {rootpth}/{midfolder}/crispr_fa')
    for bfile in os.listdir(f'{bfolder}'):
        prefix = bfile.rsplit('.', 1)[0]
        outputfile = prefix + '.crispr'

        os.system(f'java -cp {dbdir}/CRT1.2-CLI.jar crt {bfolder}/{bfile} {rootpth}/{midfolder}/crispr_tmp/{outputfile}')

        crispr_rec = []
        with open(f'{rootpth}/{midfolder}/crispr_tmp/{outputfile}') as file_in:
            for line in file_in:
                if line.startswith('ORGANISM:'):
                    accession = line.split(' ')[2]
                    cnt = 0
                else:
                    tmp_list = line.split("\t")
                    try:
                        _ = int(tmp_list[0])
                        if tmp_list[3] == '\n':
                            continue
                        rec = SeqRecord(Seq(tmp_list[3]), id=f'{prefix}_CRISPR_{cnt}', description='')
                        cnt += 1
                        crispr_rec.append(rec)
                    except:
                        continue
                        
        if crispr_rec:
            SeqIO.write(crispr_rec, f"{rootpth}/{midfolder}/crispr_fa/{prefix}_CRISPRs.fa", 'fasta')

    rec = []
    for file in os.listdir(f'{rootpth}/{midfolder}/crispr_fa/'):
        for record in SeqIO.parse(f'{rootpth}/{midfolder}/crispr_fa/{file}', 'fasta'):
            rec.append(record)
    if rec:
        SeqIO.write(rec, f"{rootpth}/{midfolder}/CRISPRs.fa", 'fasta')
    else:
        print('No CRISPRs found in the contigs.')
        exit(0)

else:
    print("Parameters Error!")
    exit(0)




# construct database and run blast
os.system(f'makeblastdb -in {rootpth}/{midfolder}/CRISPRs.fa -dbtype nucl -parse_seqids -out {rootpth}/{midfolder}/crispr_db/allCRISPRs')
