function snbpssm(filename1,filename2,filename3,filename4) %strpssm('2xfz.pdb','Y','strpssmRB111_1.xlsx','2xfz_y');基于包括内部残基的距离近邻的strpssm %
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
        posall=[posall;position];   %垂直向连接，每一分量有相同的列数
    end
end
m=size(posall);
for i=1:m
    for j=1:m
        dis(i,j)=sqrt(sum((posall(i,:)-posall(j,:)).^2));
    end
end
[QQ QC]=sort(dis,2,'ascend');%QQ:排序距离值，QC位置，QP前五个距离值，QPP前五位置%
QP= QQ(:,1:25);%改‘%%’选出距离最近的前n个，1:15就是前15，改变数量就可改变前个残基%
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
xlswrite(strcat(filename1(1:6),'_SNB-PSSM.xlsx'),PSSM,filename1(1:6)); %输出xls文件;
fclose('all');
end