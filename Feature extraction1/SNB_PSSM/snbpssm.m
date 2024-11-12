function snbpssm(filename1,filename2,filename3,filename4) %strpssm('2xfz.pdb','Y','strpssmRB111_1.xlsx','2xfz_y');���ڰ����ڲ��л��ľ�����ڵ�strpssm %
fclose('all');
fid1=fopen(filename1,'r');
MAX=1000000;
posall=[];
for i=1:MAX
    pdb=fgetl(fid1);
    if pdb(1)=='E'& pdb(2)=='N'& pdb(3)=='D'
        break;
    elseif length(pdb)<3
        continue;
    elseif ((pdb(1:4)=='ATOM')&(pdb(14)=='C')&(pdb(15)=='A')&(pdb(22)==filename2))
        position=[str2num(pdb(31:38)) str2num(pdb(39:46)) str2num(pdb(47:54))];
        posall=[posall;position];   %��ֱ�����ӣ�ÿһ��������ͬ������
    end
end
m=size(posall);
for i=1:m
    for j=1:m
        dis(i,j)=sqrt(sum((posall(i,:)-posall(j,:)).^2));
    end
end
[QQ QC]=sort(dis,2,'ascend');%QQ:�������ֵ��QCλ�ã�QPǰ�������ֵ��QPPǰ��λ��%
QP= QQ(:,1:25);%�ġ�%%��ѡ�����������ǰn����1:15����ǰ15���ı������Ϳɸı�ǰ���л�%
QPP=QC(:,1:25);%%
pssm=xlsread(filename3,filename4);
PSSM=[];
for i=1:length(pssm)
    P=[];
    for j=1:25 %%
        p=pssm(QPP(i,j),:);
        P=[P p];
    end
    PSSM=[PSSM;P];
end
xlswrite(strcat(filename4(1:6),'_SNB-PSSM.xlsx'),PSSM,filename4(1:6)); %���xls�ļ�;
fclose('all');
end