# MFEPre:
Multi-feature enhanced protein language models for accurate protein-RNA binding residue prediction

## protein feature extraction

The feature extraction code can be found in the folder, and the top 20 feature files obtained are provided

### 1.PSSM

Go to the website https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome to get a pssm file.
Here, select "PSI-BLAST" for "Program Selection" item, and use default parameters for other items.

### 2.SNB-PSSM
Go to the website https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome to get a pssm file named 2l5d_a.asn_matrix.txt 
calculate SNB-PSSM-based features in MATLAB, follow these steps:
Run clash analysis: 
In MATLAB, execute：clash('2l5d_a.pdb', 'A', '2l5d_a.asn_matrix.txt')，This generates 2l5d_a.xlsx.
Calculate SNB-PSSM:
snbpssm('2l5d_a.pdb', 'A', '2l5d_a.xlsx', '2l5d_a')，This generates 2l5d_a_SNB-PSSM.xlsx.
Make sure all necessary files (clash.m, snbpssm.m, 2l5d_a.pdb, 2l5d_a.asn_matrix.txt) are in the same folder.

### 3. CX/DPX
The folder provides the complete feature extraction software “psaia” and install the program "psaia.exe".
a. Run "psaia.exe";
b. Step by step, selecet "Structure Analyser" tab control, then find "Analysis Types" and check both "Analyse as Bound" and "Analyse by Chain". All parameters are set to default;
c. Input the pdb file "4JVH_A.pdb" (hydrogen atoms removed) to the program, and click "run" to get the result

### 4.Topology
Run "GNtopology.py" with "2AZ0_A.pdb" as input file (keep "IP.py" and "2AZ0_A.pdb" in the same folder).

### 5. IP
Run "IP.py" with "2AZ0_A.pdb" as input file (keep "IP.py" and "2AZ0_A.pdb" in the same folder).

### 6.Dynamics
In this case, 2l5d_a.pdb is the protein structure file that is located in the same folder as the MATLAB .m scripts. The output of this command will be saved in a text file called 2l5d_a_dynamics.txt, 
which contains the dynamic features calculated using the GNM.

### 7.protbert embedding
a： To run ProtBERT_feature_generator.py, follow these steps:
    Prerequisites:
    Install required dependencies: Ensure you have Python installed (preferably Python 3.6+). You will also need to install the required Python libraries, 
    such as transformers, torch, and biopython. You can install them using pip: pip install torch transformers biopython
    
b:  Download ProtBERT Model: The ProtBERT_feature_generator.py script likely uses a pre-trained ProtBERT model. You can download it from the Hugging Face Model Hub.

### 8. protein graph embedding 
Input protein nodes and edge data into graph neural network to obtain protein graph embedding features


## Help

For any questions, please contact us by 0430078017@stu.ahau.edu.cn.
