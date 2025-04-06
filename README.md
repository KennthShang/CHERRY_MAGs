# ATTNETION!!!
- The program has been updated and moved to [PhaBOX 2](https://github.com/KennthShang/PhaBOX), which is more user-friendly. In the new version, PhaMer is generalized to all kinds of viruses, more than just phages. Hope you will enjoy it. This folder will be no longer maintained. 


- Our web server for viruses-related tasks (including virus identification, taxonomy classification, lifestyle prediction, host prediction, and protein annotation) is available! You can visit [Web Server](http://phage.ee.cityu.edu.hk/) to use the GUI. We also provided more detailed intermediate files and visualization for further analysis.


# CHERRY_MAGs
This is the MAGs version of CHERRY. You can use this version on your own bacterial assemblies and predict the interactions between your phages and your bacteria.

## Required Dependencies

* Python 3.x
* Java

## An easier way to install

We suggest you install all the packages using conda (both Miniconda and Anaconda are okay) following the command lines below:

```
cd CHERRY_MAGs
conda env create -f CHERRY.yaml -n cherry
conda activate cherry
cd dataset
bzip2 -d protein.fasta.bz2
bzip2 -d nucl.fasta.bz2
cd ..
```

**Noted:** You still need to install Java if your device does contain such an env

## Usage
### 1 Predicting host for your viruses
The input should be a fasta file containing the viral sequences. We provide an example file named "test_contigs.fa". Then, the only command that you need to run is 

    python run_Speed_up.py [--contigs INPUT_FA] [--len MINIMUM_LEN] [--model MODEL] [--topk TOPK_PRED]
    
**Options**


      --contigs INPUT_FA
                            input fasta file
      --len MINIMUM_LEN
                            predict only for sequence >= len bp (default 8000)
      --model MODEL (pretrain or retrain)
                            predicting host with pretrained parameters or retrained paramters (default pretrain)
      --t THRESHOLD
                            The threshold for a confident prediction (default 0.5)
      --topk TOPK_PRED
                            The host prediction with topk score (default 1)

               
## Predicting the interactions between your viruses and prokaryotes/MAGs
You should replace the genomes provided in the `prokaryote/` folder with your own prokaryotes/MAGs. Then, you can run with the same command as mentioned above.

However, please always remember that you still need to update the accession of your prokaryotes/MAGs to the *dataset/prokaryote.csv* file. The rule and an example can be found below.

**Example**

If you have metagenomic data and you know that only E. coli exist in the metagenomic data. Then, you can place the genomes of these three species into the *prokaryote/* and add the entry in *dataset/prokaryote.csv*. An example of the entry looks like:

    GCF_000007445,Bacteria,Proteobacteria,Gammaproteobacteria,Enterobacterales,Enterobacteriaceae,Escherichia,Escherichia coli

The corresponding header of the entry is: Accession, Superkingdom, Phylum, Class, Order, Family, Genus, Species. 

If you do not know the whole taxonomy tree, you can directly use a specific name for all columns. For example, if you only have a bacteria assembly named **Bin2077.fa**, then the entry can be:

    Bin2077,Bin2077,Bin2077,Bin2077,Bin2077,Bin2077,Bin2077,Bin2077

    
## Common problems
***Noted one*** Since our program will use the "accession" for searching and constructing the knowledge graph, the name of the fasta file of your genomes should be the same as the given "accession" in the CSV file. For example, if your accession in CSV is GCF_000007445, your file name should be GCF_000007445.fa. Otherwise, the program cannot find the entry. 

***Noted two*** Also, please **DO NOT** use special characters; otherwise, it might raise unexpected errors. Also, please replace all the '.' with "_" in the name of your MAGs. For example, please do not use "bin.4.2.xxx.2.fa" but use "bin_4_2_xxx_2.fa"


