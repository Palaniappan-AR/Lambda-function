a=[1,2,3,4,5,6,7,8,9,10]
b=lambda x:x*3
c=map(b,a)
print('Output 1:',list(c))

x=lambda x:x**2
print('Output 2:')
for i in range(1,11):
    print(x(i))

y=[1,2,3,4,5,6,7,8,9,10]
print('Output 3:',list(map(lambda x:x%2!=0,y)))

'''Output of above program:
    
Output 1: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

Output 2:
1
4
9
16
25
36
49
64
81
100

Output 3: [True, False, True, False, True, False, True, False, True, False]'''
