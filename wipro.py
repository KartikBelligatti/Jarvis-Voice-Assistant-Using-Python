# # fibonacci
# def fib(n):
#
#     if(n<0):
#         print("invalid")
#     elif(n==0):
#         return 0
#     elif(n==1 or n==2):
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# n=int(input())
# print(fib(n))


#
# # Polymorphism
# class India():
# 	def capital(self):
# 		print("New Delhi is the capital of India.")
#
# 	def language(self):
# 		print("Hindi is the most widely spoken language of India.")
#
# 	def type(self):
# 		print("India is a developing country.")
#
# class USA():
# 	def capital(self):
# 		print("Washington, D.C. is the capital of USA.")
#
# 	def language(self):
# 		print("English is the primary language of USA.")
#
# 	def type(self):
# 		print("USA is a developed country.")
#
# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
# 	country.capital()
# 	country.language()
# 	country.type()



# # binary to decimal
# def dtb(n):
# 	if n>=1:
# 		dtb(n//2)
# 	print(n%2,end='')
# n=int(input())
# dtb(n)






# #factorial of a number
# def fac(n):
# 	if(n==1 or n==0):
# 		return 1
# 	else:
# 		return n*fac(n-1)
# n=int(input())
# print(fac(n))




#Armstrong number

n = input()
sum=0
for i in range(len(n)):
    sum+=int(n[i])** len(n)
print(sum)