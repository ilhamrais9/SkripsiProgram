clc; close all;

a=dlmread('rafliB1.txt');
a1=a(:,1);
a2=a(:,2);

fs=1479;

b=filter(Hd,a1);
c=b(500:20000);
d=mean(c);
e=c-d;

e1=abs(e)

j=1;

for j=j:19000;
    k=j+500
    e2=e1(j:k);
    mov(:,j)=mean(e2);
    
end
l=1;
for l=l:length(mov)-501
    rms(:,l)=sqrt(mean(mov(l:l+500).^2));
end
subplot 211
plot(b)
ylim([-20,20])
subplot 212
plot(rms)
% ylim([-20,20])