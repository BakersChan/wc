#include<stdio.h>
int main()
{
int a,i,j,sum=0;
double eavg;
int b[5],temp;
printf("请输入5个正整数\n");
for(i=0;i<5;i++){
scanf("%d",&b[i]);
sum+=b[i];
}
for(j=0;j<4;j++)
for(i=0;i<4-j;i++)
if(b[i]<b[i+1])
{
temp=b[i];
b[i]=b[i+1];
b[i+1]=temp;
}
printf("1,求和\n2,求平均值\n3,查询最大值\n4,查询最小值\n");
scanf("%d",&a);
switch(a)
{
case 1:
printf("累计和%d\n",sum);
break;
case 2:
eavg=(double)sum/5;
printf("平均值为%f\n",eavg);
break;
case 3:
printf("数组中最大值为%d\n",b[0]);
break;
case 4:
printf("数组中最小值为%d\n",b[4]);
break;
}
for(i=0;i<5;i++)
printf("%d ",b[i]);
return 0;
}