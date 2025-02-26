# num=int(input('enter the digit'))
# sum=0
# product=1
# while(num>0):
#     b=num%10
#     sum=sum+b
#     product=product*b
#     num=num//10
# if sum==product:
#    print('number is spy')
# else:
#     print('not spy')

# from collections import Counter
# a=[1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]
# b=Counter(a)
# print(b)

# def countDigit(n):
#     if n//10==0:
#         return 1
#     return 1+countDigit(n//10)
# if __name__=="__main__":
#  n=5896443
# print(countDigit(n))    


# a=[10,30,50,90,20]
# max_element=a[0]
# for i in range(len(a)):
#  if a[i] >max_element:
#         max_element=a[i]
# print(max_element)


# a=[10,30,50,90,20]
# a.sort(reverse=True)
# print(a[1])

# n=int(input('enter the range'))
# for i in range(n+1):
#   for j in range(i-1):
#        print('*+*+',end='')
# print()


# for i in range(1,5):
#     for j in range(4-i):
#         print(end='')
#     for j in range(1,i*2):
#         print('*',end='')
#     print()
# for i in range(3,0,-1):
#     for j in range(4-i):
#         print(end='')
#     for j in range(1,i*2):
#         print('*',end='')
#     print()


# for i in range(5):
#     for j in range(i+1):
#      print('* ',end='')
#     print()

