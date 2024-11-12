function [posall,resall]=pdbread(filename)
fclose('all');
fid1=fopen(filename,'r');
MAX=100000;
resall=[];
posall=[];
for i=1:MAX
pdb=fgetl(fid1);
if pdb(1)=='E'&pdb(2)=='N'&pdb(3)=='D'
    break;
elseif pdb(1)=='T'&pdb(2)=='E'&pdb(3)=='R'
    break;
elseif length(pdb)<3
    continue;
elseif ((pdb(1:4)=='ATOM')&((pdb(14)=='C')&(pdb(15)=='A')))  %% 14,15 CA 目的是读入手型c原子 而忽略其他原子                                                                                                              
    pdbname=pdb(18:20);              %我现在有一个疑问，就是抽取RNA 的 P进行粗粒化，那么P怎么命名啊？？？？？？
    if pdbname=='GLY'
            resname='G';
        elseif pdbname=='ALA'
            resname='A';
        elseif pdbname=='VAL'
            resname='V';
            elseif pdbname=='LEU'
            resname='L';
            elseif pdbname=='ILE'
            resname='I';
            elseif pdbname=='PRO'
            resname='P';
            elseif pdbname=='PHE'
            resname='F';
            elseif pdbname=='TRP'
            resname='W';
            elseif pdbname=='TYR'
            resname='Y';
            elseif pdbname=='SER'
            resname='S';
            elseif pdbname=='THR'
            resname='T';
            elseif pdbname=='CYS'
            resname='C';
            elseif pdbname=='MET'
            resname='M';
            elseif pdbname=='ASN'
            resname='N';
            elseif pdbname=='GLN'
            resname='Q';
            elseif pdbname=='ASP'
            resname='D';
            elseif pdbname=='GLU'
            resname='E';
            elseif pdbname=='HIS'
            resname='H';
            elseif pdbname=='LYS'
            resname='K';
            elseif pdbname=='ARG'
            resname='R';
            elseif pdbname=='  A' 
            resname='a';
            elseif pdbname=='  G'
            resname='g';
            elseif pdbname=='  C'
            resname='c';
            elseif pdbname=='  U'
            resname='u';
        else
            resname='B';
        end
    position=str2num(pdb(30:54));
    resall=[resall resname];   %水平向链接，每一分量有相同的行数
    posall=[posall;position];   %垂直向连接，每一分量有相同的列数
end
end

fclose('all');