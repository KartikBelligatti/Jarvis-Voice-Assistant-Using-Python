#
# #

#
# # s=input()
# # st=''
# # for i in range(len(s)-1, -1,-1) :
# #     st+=s[i]
# # print(st)
#
# #
# # def newString(s, k):
# #     X = ""
# #
# #     while (len(s) > 0):
# #         temp = s[0]
# #
# #         i = 1
# #         while (i < k and i < len(s)):
# #             if (s[i] < temp):
# #                 temp = s[i]
# #
# #             i += 1
# #
# #         X = X + temp
# #
# #         for i in range(k):
# #             if (s[i] == temp):
# #                 s = s[0:i] + s[i + 1:]
# #                 break
# #
# #     return X
# #
# # s = input()
# # k = 2
# # print((s, k))
# # #
#
#
# # num = int(input())
# # sum = 0
# # temp = num
# # while temp > 0:
# #     digit = temp % 10
# #     sum += digit ** 3
# #     temp //= 10
# # s=0
# # if num == sum:
# #     n=str(num)
# #     for i in range(len(n)):
# #         if(int(n[i])%2==0):
# #             s+=int(n[i])
# #     print(s)
# # else:
# #     n = str(num)
# #     for i in range(len(n)):
# #         if (int(n[i]) % 2 != 0):
# #             s += int(n[i])
# #     print(s)
#
#
#
#
# # n=int(input())
# # a = list(map(int,input().strip().split()))[:n]
# # c1=0
# #
# # for i in range(n):
# #     if(a[i]>0):
# #         c1+=1
# #
# # print(c1)
#
#
# # num = int(input("Enter a number: "))
# # sum = 0
# # temp = num
# #
# # while temp > 0:
# #     digit = temp % 10
# #     sum += digit ** 3
# #     temp //= 10
# #
# # if num == sum:
# #     print(num, "is an Armstrong number")
# # else:
# #     print(num, "is not an Armstrong number")
# #
# # for i in range(6):
# #     for j in range(0,i+1):
# #
# #         print("*", end="")
# #
# #
# #
# #     print("")
#
# # for row in range(1, 6):
# #     num = 1
# #     for j in range(6, 0, -1):
# #         if j > row:
# #             print(" ", end="")
# #         else:
# #             print("#", end="")
# #             num += 1
# #     print("")
#
#
#
# # n=int(input())
# # arr = list(map(int, input().rstrip().split()))[:n]
# # a=sorted(arr)
# # s=0
# # s1=0
# # for i in range(0, 4):
# #     s+=a[i]
# # for i in range(n-4,n):
# #     s1+=a[i]
# #
# #
# # print(s,s1)
#
# # s='04:05:45AM'
# # n = len(s)
# # t = s[n - 2] + s[n - 1]
# #
# # if (t == 'PM'):
# #     if (int(s[0] + s[1]) == 12):
# #         print(s[:n - 2])
# #     else:
# #         time = 12 + int(s[0] + s[1])
# #         tq=str(time)
# #         print(str(time) + s[2:n - 2])
# # if (t == 'AM'):
# #     if(int(s[0] + s[1])==12):
# #         time = 12 - int(s[0] + s[1])
# #         print(str(0) + str(time) + s[2:n - 2])
# #     else:
# #         print(s[:n - 2])
#
# #
# # n=int(input())
# # s=[]
# # for i in range(n):
# #    s.append(int(input()))
# # for i in range(n):
# #     r=s[i]%5
# #     r1=5-r
# #     if(r1<3 and s[i]>=38):
# #         s[i]=s[i]+r1
# #         print(s[i])
# #     else:
# #         print(s[i])
#
#
# # s = int(input())
# # t = int(input())
# # a = int(input())
# # b = int(input())
# # m = int(input())
# # n = int(input())
# # apples = list(map(int, input().rstrip().split()))
# # oranges = list(map(int, input().rstrip().split()))
# # c=0
# # c1=0
# # for i in range(m):
# #     if(a-apples[i]>=s and a-apples[i]<=t ):
# #         c+=1
# # for i in range(n):
# #     if(b-oranges[i]>=s and b-oranges[i]<=t):
# #         c1+=1
# # print(c,c1)
#
#
#
# # x1=int(input())
# # v1=int(input())
# # x2=int(input())
# # v2=int(input())
# # n=0
# # f=True
# # for i in range(n):
# #     x1+=v1
# #     x2+=v2
# #     if(x1==x2):
# #         print("YES")
# #         break
# #     else:
# #         f=False
# #     n+=1
# # if(f==False):
# #     print("NO")
#
#
# # n=int(input())
# # s=''
# # for i in range(n):
# #     s+=str(i+1)
# # print(s)
# from itertools import combinations
#
# # s,n=input().split()
# # n=int(n)
# # vals=list(combinations(sorted(s),n))
# # r=[]
# # res=[]
# # for x in s:
# #     r.append(''.join(x))
# # for x in vals:
# #     res.append(''.join(x))
# #
# # print('\n'.join(sorted(r)))
# # print('\n'.join(sorted(res)))
#
#
#
# # s=input()
# # n=int(input())
# # for i in range(n):
# #     for j in range(n):
# #         if(i!=j):
# #             print(s[i]+s[j])
#
#
# # from itertools import combinations_with_replacement
# # s,n=input().split()
# # n=int(n)
# # vals=list(combinations_with_replacement(sorted(s),n))
# # r=[]
# # res=[]
# # for x in s:
# #     r.append(''.join(x))
# # for x in vals:
# #     res.append(''.join(x))
# #
# # # print('\n'.join(sorted(r)))
# # print('\n'.join(sorted(res)))
#
#
#
#
# #
# # n=input()
# #
# # for i in range(len(n)):
# #     for j in range(i, len(n)):
# #         if(i!=j):
# #             if(n[i]==n[j]):
# #                 n.translate({j: None})
# # print(n)
#
#
# # from itertools import permutations
# #
# # x = int(input())
# # y = int(input())
# # z = int(input())
# # # n = int(input())
# # print(permutations(x, y, z))
#
#
#
#
# #
# # input1=int(input())
# # input2=int(input())
# # input3=int(input())
# # ans=0
# # ans=input1**input2
# # return ans%input3
# #
# #
# #
# # pass True
#
#
# def decToBinary(n):
#     # array to store
#     # binary number
#     binaryNum = [0] * n;
#
#     # counter for binary array
#     i = 0;
#     while (n > 0):
#         # storing remainder
#         # in binary array
#         binaryNum[i] = n % 2;
#         n = int(n / 2);
#         i += 1;
#
#     # printing binary array
#     # in reverse order
#     for j in range(i - 1, -1, -1):
#         print(binaryNum[j], end="");
#
#
# # Driver Code
# n = 17;
# decToBinary(n);





















n=input()
s = ''
for i in range(len(n)-1, -1, -1):
    s=s+n[i]
print(s)