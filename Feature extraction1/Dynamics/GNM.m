function GNM(filename) %GNM(filename)
[posall,resall]=pdbread(filename);
n1=length(resall);
netmat1=zeros(n1);
m=[];
fluslown=[];
m=abs(resall);
for i=1:n1
    for j=i:n1
        if i==j
            continue;
        else
            dis=juli(posall(i,:),posall(j,:));
            x=1/dis^2;
            netmat1(i,j)=-x;
            netmat1(j,i)=-x;
        end
    end
end
for i=1:n1
    netmat1(i,i)=-1*sum(netmat1(i,:));
end
[V,D]=eig(netmat1);
for i=1:n1
    fluslow1(i)=0;
    fluslow1(i)=fluslow1(i)+V(i,2)*V(i,2)/D(2,2);
end
s1=fluslow1';
for i=1:n1
    fluslow2(i)=0;
    for j=2:3
        fluslow2(i)=fluslow2(i)+V(i,j)*V(i,j)/D(j,j);
    end
end
s2=fluslow2';
for i=1:n1
    fluslow3(i)=0;
    for j=2:4
        fluslow3(i)=fluslow3(i)+V(i,j)*V(i,j)/D(j,j);
    end
end
s3=fluslow3';
for i=1:n1
    fluslow4(i)=0;
    for j=2:5
        fluslow4(i)=fluslow4(i)+V(i,j)*V(i,j)/D(j,j);
    end
end
s4=fluslow4';
for i=1:n1
    fluslow5(i)=0;
    for j=2:6
        fluslow5(i)=fluslow5(i)+V(i,j)*V(i,j)/D(j,j);
    end
end
s5=fluslow5';
for i=1:n1
    fluslow6(i)=0;
    for j=2:7
        fluslow6(i)=fluslow6(i)+V(i,j)*V(i,j)/D(j,j);
    end
end
s6=fluslow6';
S=[s1,s2,s3,s4,s5,s6];  %输出前六种运动模式
TXT = fopen(strcat(filename(1:6),'_dynamics.txt'),'wt'); %输出到txt文件；
for  i = 1:size(S,1)
    for j = 1:size(S,2)
        fprintf(TXT,'%6.4f  ',S(i,j));
    end
    fprintf(TXT,'\n');
end
fclose(TXT);
end

























