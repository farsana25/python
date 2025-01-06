# for i in range(5):
#     print('Farsana')

# sum=0
# a=[1,2,3,4,5]
# for i in (a):
#     sum=sum+i
# print(sum)


# a=4
# while a<8:
#     print(a)
#     a=a+1
# sum=0
# a=[]
# for i in range(5):
#    b=int(input('enter the value'))
#    a.append(b)
# print(b)
# for i in (a):
#   sum=sum+i
# print(sum)

# a=[]
# for i in range(5):
#  b=int(input('enter the value'))
#  a.append(b)
#  print(a)

# sum=0
# a=[]
# for i in range(5):
#     b=int(input('enter the value'))
#     a.append(b)
#     print(b)
#     for i in (a):
#         sum=sum+i
#         print(sum)

# for i in range(2,30,3):
#     print(i)

# a='red','big','tasty'
# b='apple','banana','cherry'
# for i in a:
#     for j in b:
#         print(i,j)


# numbers=[2,8,12,4,6]
# largest=numbers[0]
# for num in numbers:
#  if num>largest:
#      largest=num
# print('largest number is:',largest)

# numbers=[1,2,3,4,1,2,2,3,4,1,2,4]
# count=numbers.count(2)
# print('occures',count,'times in list')


# numbers=[1,3,1,2,5,1,6,3,4,1,2]
# element_to_count=2
# count=0
# for element in numbers:
#     if element==element_to_count:
#         count+=1
#         print('occures',element_to_count,count)


# a=[1,1,1,2,2,2,3,3,4,4,4,5,5]
# count=0
# k=len(a)
# b=int(input('enter element'))
# for i in range(k):
#     if a[i]==b:
#         count=count+1
#         print('the elements',b,'occurs',count,'times')


a=input('enter the word:')
for i in (a):
    if(a.count(i)==1):
        print(i,end='')





