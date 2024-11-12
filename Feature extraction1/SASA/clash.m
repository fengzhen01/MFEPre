function clash(filename1,filename2,filename3) %('1.pdb','A','pssm.txt')这个程序坐标读取准确，可用.基于距离近邻的pssm矩阵%
fclose('all');
posall=[];
row=1000000;
fid1=fopen(filename1,'r');
for i=1:row
    pl=fgetl(fid1);
    if ((pl(1:3)=='END')|(pl(1:3)=='TER'))
        break;
    elseif(((pl(1:4)=='ATOM')&(pl(14)=='C')&(pl(15)=='A')&(pl(22)==filename2)))
        pos=[str2num(pl(31:38)) str2num(pl(39:46)) str2num(pl(47:54))];
        posall=[posall;pos];
    end
end
fclose('all');
m=size(posall);
for i=1:m
    for j=1:m
        dis(i,j)=sqrt(sum((posall(i,:)-posall(j,:)).^2));
    end
end
[row,col] = find(dis<7.5);
[number,types,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20]=textread(filename3,'%d %s %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d','delimiter', '\t','headerlines', 1);
pssm=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20];
D=pssm(row,:);
k = find([true;diff(col(:))~=0;true]);
n=size(k);
for i=1:n-1
    PSSM(i,:)=mean(D(k(i):k(i+1)-1,:));
end
xlswrite(strcat(filename1(1:6),'.xlsx'),PSSM,filename1(1:6)); 
fclose('all');
end








