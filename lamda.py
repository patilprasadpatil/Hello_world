# Simple message passing:
print('-------------------------------------')
show = lambda : print("Hello")
print(show())
print('-------------------------------------')

# With passing arguments:
add = lambda x,y : x+y
print(add(30,20))
print('-------------------------------------')

# Using multiple expressions:
add_sub = lambda x,y : (x+y,x-y,x*y,x/y,x%y)
print(add_sub(16,5))
print('-------------------------------------')

# Using multiple expressions(different pattern):
a_s_m_d_m = lambda x,y : (x+y,x-y,x*y,x/y,x%y)
add,sub,mul,div,mod = a_s_m_d_m(16,5)

print("Addition is: ",add)
print('Substraction is:',sub)
print('Multiplication is:',mul)
print('Division is:',div)
print('Mod is:',mod)
print('-------------------------------------')




