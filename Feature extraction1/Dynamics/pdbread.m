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
elseif ((pdb(1:4)=='ATOM')&((pdb(14)=='C')&(pdb(15)=='A')))  %% 14,15 CA Ŀ���Ƕ�������cԭ�� ����������ԭ��                                                                                                              
    pdbname=pdb(18:20);              %��������һ�����ʣ����ǳ�ȡRNA �� P���д���������ôP��ô������������������
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
    resall=[resall resname];   %ˮƽ�����ӣ�ÿһ��������ͬ������
    posall=[posall;position];   %��ֱ�����ӣ�ÿһ��������ͬ������
end
end

fclose('all');