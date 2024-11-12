#coding:utf-8
import numpy as np
import xlsxwriter
pdb=open('2l5d_a.pdb', 'r')
content=pdb.read()
pdb.close
line= content.strip().split("\n")
A_i=[]
for i in range(0,len(line)):
    if line[i][0:4]=='ATOM' and ((line[i][13] == 'C' and line[i][14] == 'A')):    #
        pdbname=line[i][17:20]
        if  pdbname =='GLY':
            resname='G'
            A=[0,1,0.12,0.5,0.901,7.9,0.58,2.4,0,0.9,0.005]
        elif  pdbname =='ALA':
            resname='A'
            A=[0,1,2.01,0.328,0.937,7,0.22,0.35,-0.01,1.6,0.0373]
        elif  pdbname=='VAL':
            resname='V'
            A=[0,0.6,3.5,0.946,0.625,5.6,0.08,0.43,0.01,0.6,0.0057]
        elif pdbname=='LEU':
            resname='L'
            A=[0,1,2.73,0.414,0.808,4.9,0.19,0.58,-0.01,0.3,0]
        elif pdbname=='ILE':
            resname='I';
            A=[0,0.6,3.7,2.078,0.178,4.9,0.22,0.12,-0.01,0.7,0]
        elif pdbname=='PRO':  
            resname='P'
            A=[0,1,0.41,0.415,0.748,6.6,0.46,0.43,0,0.5,0.0198]
        elif pdbname=='PHE':
            resname='F'
            A=[0,1,2.68,1.336,0.803,5,0.08,0.89,0.03,0.9,0.0946]
        elif pdbname=='TRP':
            resname='W';
            A=[0,1,2.49,1.781,0.803,5.3,0.43,0.62,0,1.7,0.0548]
        elif pdbname=='TYR':
            resname='Y'
            A=[0,1,2.23,0,1.227,5.7,0.46,1.44,0.03,0.4,0.0516]
        elif pdbname=='SER':
            resname='S'
            A=[0,1.7,1.47,1.089,1.145,7.5,0.55,1.24,0.11,0.8,0.0829]
        elif pdbname=='THR':
            resname='T'
            A=[0,1.7,2.39,1.732,1.487,6.6,0.49,0.85,0.04,0.7,0.0941]
        elif pdbname=='CYS':
            resname='C'
            A=[0,1,1.98,0,1.004,5.5,0.2,0.5,0.12,1.2,0.0829]
        elif pdbname=='MET':
            resname='M'
            A=[0,1,1.75,0.982,0.886,5.3,0.38,0.22,0.04,1,0.0823]
        elif pdbname=='ASN':
            resname='N'
            A=[0,1.7,0.03,1.498,1.08,10,0.42,2.12,0.06,0.7,0.0036]
        elif pdbname=='GLN':
            resname='Q'
            A=[0,1,1.02,0,1.078,8.6,0.26,0.73,0.05,0.8,0.0761]
        elif pdbname=='ASP':
            resname='D'
            A=[-1,3.2,-2.05,3.379,1.64,13,0.73,2.16,0.15,2.6,0.1263]
        elif pdbname=='GLU':
            resname='E'
            A=[-1,1.7,0.93,0,0.679,12.5,0.08,0.65,0.07,2,0.0058]
        elif pdbname=='HIS':
            resname='H'
            A=[1,1,-0.14,1.204,1.085,8.4,0.14,1.19,0.08,0.7,0.0242]
        elif pdbname=='LYS':
            resname='K'
            A=[1,0.7,2.55,0.835,1.254,10.1,0.27,0.83,0,1,0.0371]
        elif pdbname=='ARG':
            resname='R'
            A=[1,0.7,0.84,2.088,1.725,9.1,0.28,0.75,0.04,0.9,0.0959]
        A_i.append(A)
print(A_i)
A_i=np.array(A_i)
workbook = xlsxwriter.Workbook('2l5d_a_AA_index.xlsx')
worksheet = workbook.add_worksheet('AA_index')
for i in range(A_i.shape[0]):
    for j in range(A_i.shape[1]):
        worksheet.write(i,j,A_i[i][j])
workbook.close()


