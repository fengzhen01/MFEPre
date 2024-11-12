#!/usr/bin/env python
#    -*- coding:utf-8 –*-

import os
import math
import numpy
import networkx as nx


# construct adjacent matrix
def create_matrix(number, amount):
    matrix = []
    for i in range(0, number):
        tmp = []
        for j in range(0, number):
            tmp.append(amount)
        matrix.append(tmp)
    return matrix

def pdbread(filename):
    pdb=open(filename, 'r')
    content=pdb.read()
    pdb.close
    line= content.strip().split("\n")
    List=[]
    node_list=[]
    for i in range(0,len(line)):
        if line[i][0:4]=='ATOM' and ((line[i][13] == 'C' and line[i][14] == 'A')): 
            pdbname=line[i][17:20]
            '''
        if  line[i][21]=='B' and line[i][24:26]=='53':
            continue
            '''
            if  pdbname =='GLY':
                resname='G'
            elif  pdbname =='ALA':
                resname='A'
            elif  pdbname=='VAL':
                resname='V' 
            elif pdbname=='LEU':
                resname='L'
            elif pdbname=='ILE':
                resname='I';
            elif pdbname=='PRO':  
                resname='P'
            elif pdbname=='PHE':
                resname='F'
            elif pdbname=='TRP':
                resname='W';
            elif pdbname=='TYR':
                resname='Y'
            elif pdbname=='SER':
                resname='S'
            elif pdbname=='THR':
                resname='T'
            elif pdbname=='CYS':
                resname='C'
            elif pdbname=='MET':
                resname='M'
            elif pdbname=='ASN':
                resname='N'
            elif pdbname=='GLN':
                resname='Q'
            elif pdbname=='ASP':
                resname='D'
            elif pdbname=='GLU':
                resname='E'
            elif pdbname=='HIS':
                resname='H'
            elif pdbname=='LYS':
                resname='K'
            elif pdbname=='ARG':
                resname='R'
            else:
                resname='B' 
            x_coord = float(line[i][30:38])
            y_coord = float(line[i][38:46])
            z_coord = float(line[i][46:54]) 
            List.append([x_coord, y_coord, z_coord])
            node_list.append(resname)   
            n=len(node_list)
    adjacent_matrix = create_matrix(n, 0)
    for i in range(len(List)):
        for j in range(len(List)):
            if i == j:
                continue
            else:
                dis = juli(List[i],List[j])
                cutoff = 7
            if dis < cutoff:
                adjacent_matrix[i][j]=1
                adjacent_matrix[j][i]=1
    return  adjacent_matrix,node_list,n

def juli(x1,x2):
    juli = float(math.sqrt((x1[0]-x2[0])**2+(x1[1]-x2[1])**2+(x1[2]-x2[2])**2))
    return  juli

if __name__ == '__main__':
    
    filePath='D:/fengzhen/MFEPre/Feature extraction/Topology/'
    filenamelist=os.listdir(filePath)
    print (filenamelist)
    for i in range(0,(len(filenamelist))):
        filename=filenamelist[i]
        adjacent_matrix,node_list,n=pdbread(filename)
        G=nx.Graph()
        G=nx.from_numpy_matrix(numpy.matrix(adjacent_matrix))
        if (nx.is_connected(G)==True):
            print ('The graph is connected.')
            Graph_information=nx.info(G)
            print (Graph_information)
            degrees =G.degree(G)
            cluster_coefficient=nx.clustering(G)
            degrees_centrality=nx.degree_centrality(G)
            closenesses_centrality=nx.closeness_centrality(G)
            betweennesses=nx.betweenness_centrality(G)
            #eigenvector_centralities=nx.eigenvector_centrality_numpy(G)
            #communicability_centralites=nx.communicability_centrality(G)
            fp=open(filename[0:6]+"_Network_statistics.txt","a")
            fp.write("tdegree\tcluster_coefficient\tdegrees_centrality\tclosenesses_centrality\tbetweennesses\n")
            for key in degrees:
                fp.write("%d\t%f\t%f\t%f\t%f\n"%(degrees[key],cluster_coefficient[key],degrees_centrality[key],closenesses_centrality[key],betweennesses[key]))

    
    
    
    
