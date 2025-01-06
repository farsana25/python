a=input('enter your name')
b=int(input('Mark of English'))
c=int(input('Mark of Malayalam'))
d=int(input('Mark of Chemistry'))
marks=b+c+d

if marks>290:
      print('You Got A+')
elif marks>280:
      print('You Got A')
elif marks>270:
      print('You Got B+')
elif marks>260:
      print('You Got B')
else:
      print("failed")