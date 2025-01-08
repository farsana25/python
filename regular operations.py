# import re
# pattern='Good'
# if re.match(pattern,'Good eve,how are you'):
#     print('yes')
# else:
#     print('sorry')




# import re
# pattern='good'
# if re.search(pattern,'hi eve,how are you good'):
#     print('yes')
# else:
#     print('sorry')



# import re
# pattern='123'
# if re.search(pattern,'There are 123 apple'):
#     print('yes,123 is found')
# else:
#     print('sorry,123 not found')


# import re
# pattern='you'
# b=re.findall(pattern,'hello how are you,where are you from,how old are you')
# print(b)
# c=len(b)
# print(c)



# import re
# a='hi muhsina who are you'
# pattern='muhsina'
# c=re.sub(pattern,'iza',a)
# print(c)


# import re
# pattern='you'
# b=re.findall(pattern,'hello how are you,where are you from,how old are you')
# a={pattern:len(b)}
# print(a)


# a=input('enter the word :')
# b=(a[::-1])
# print(b)

# word=input('enter the word: ')
# reversed_word=word[::-1]
# print(reversed_word)

# s=input('enter the word :')
# reversed_words=''.join(s.split()[::-1])
# print(reversed_words)


a=(1,2,9,8,3)
a.sort()
ans=[]
for i in range(len(a)-1,-1,-1):
    ans.append(a[i])
    print(''.join(map(str,ans)))

























