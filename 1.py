'''count,fouth=[],[]
for i in range(1,2025):
    s = bin(i)
    s=s.lstrip('0b')
    tep=0
    for i in range(len(s)):
        tep+=int(s[i])
    count.append(tep)
for i in range(1,2025):
    tep,c,s=i,0,''
    while tep %4==0:
        c+=1
        tep=tep//4
    s+=str(tep%4)
    s.join(str(0*i) for i in range(c))
    ss=0
    for i in range(len(s)):
        ss+=int(s[i])
    fouth.append(ss)
ccc=0
for i in range(2024):
    if count[i]==fouth[i]:
        ccc+=1
print(ccc)'''
#2
count = 0
for i in range(10000000,100000000):
    tep=str(i)
    if tep.find('0')==-1 and tep.find('3')!=-1 and tep.find('7')!=-1:
        count+=1
print(count)
#5
# import itertools
# t=int(input())
# s=[int(input()) for i in range(t)]
# for i in range(len(s)):
#     it = itertools.permutations([i for i in range(1,s[i]+1)])
#     count=0
#     for i in it:
#         count+=1
#     print(count)
import collections

# t=int(input())
# pepole=[]
# def check(pep,k):
#     count=0
#     for i in pep:
#         if i <k:
#            count+=1
#     if k-count<=1 and k>1:return False
#     if k==1 and count!=0:return False#z组数为1且人数小于3
#     else:
#         return True
# for _ in range(t):
#     nt,k=map(int,input().split(' '))
#     for i in range(nt):
#         a,b=map(int,input().split(' '))
#         pepole.append(b)
#     if check(pepole,k):
#         pepole=sorted(pepole)
#         index=-1
#         for i in pepole:
#             if i-3>=0:
#                 index=pepole.index(i)
#                 break
#         new_pepole=pepole[:index]
#         pre_pepole=pepole[index:]
#         if len(new_pepole)==0:
#             print(3*k+2)
#         else:
#             sum_a=sum(new_pepole)
#             res=len(pre_pepole)*3-sum(pre_pepole)-len(pre_pepole)*3+sum_a*3-sum_a
#             print(res)
#     else:
#         print(-1)
#         break
