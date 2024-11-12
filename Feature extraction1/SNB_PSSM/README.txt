SNB-PSSM is a spatial neighbor based PSSM used for protein-RNA binding site prediction.
Authors are Yang Liu, Weikang Gong, Zhen Yang and Chunhua Li.
The performance process includes two steps: generation of the SNB-PSSM and prediction performance.

Taking the binding site prediction of an RNA-binding protein for example, whose sequence file is 2xlk_a.FASTA (Here, "a" is the chain identifer. For the protein, the experimental complex structure has been solved with PDB code 2xlk). The following shows the process of the prediction.

The first step: generation of SNB-PSSM (a matrix of N*500, N is the sequence length)
Go to the website https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome to produce a pssm file named 2xlk_a.asn_matrix.txt 
Generate SNB-PSSM with the Matlab m files including clash.m and snbpssm.m. Keep 2xlk.pdb and 2xlk_a.asn_matrix.txt in the folder where Matlab m files are.
In Matlab, run the command line: clash('2xlk.pdb','A','2xlk_a.asn_matrix.txt'), and get 2xlk_a.xlsx (a smoothed matrix of N*20). Then, run the command line: snbpssm('2xlk.pdb','A','2xlk_a.xlsx','2xlk_a'), and get 2xlk_a_SNB-PSSM.xlsx (a matrix of N*500, N is the sequence length).
Then, open the  2xlk_a_SNB-PSSM.xlsx, and create a new sheet named as "label", and put the label (1 or 0 for binding or unbinding sites) of 2xlk_a in the new sheet. 

The second step: prediction performance (with the trained model)
Open Matlab progarm, command line: load('SNB-PSSM.mat')
If the label is known and you want to compare the true and predicted resutls, then perform the following steps: 
In order to read the label for 2xlk_a
command line: test2xlkl=xlsread('2xlk_a_SNB-PSSM.xlsx','label','a1:a188'); 
In order to read the SNB-PSSM for 2xlk_a
command line: test2xlk=xlsread('2xlk_a_SNB-PSSM.xlsx','2xlk','a1:sf188');
In order to produce the prediction result of 2xlk_a, keep SNB-PSSm.mat and 2xlk_a_SNB-PSSM.xlsx in the same folder. 
command line: [predict_label,accuracy] = svmpredict(test2xlkl,test2xlk,model);   
The outputs are two files: predict_label  where the prdicted RNA-binding sites are stored, and accuracy file

If the label is not known, then perform the following steps: 
In order to read the SNB-PSSM for 2xlk_a
command line: test2xlk=xlsread('2xlk_a_SNB-PSSM.xlsx','2xlk','a1:sf188');
In order to produce the prediction result of 2xlk_a, keep SNB-PSSm.mat and 2xlk_a_SNB-PSSM.xlsx in the same folder. 
command line: [predict_label] = svmpredict(test2xlk,model);   
The output is predict_label where the prdicted RNA-binding sites are stored.

