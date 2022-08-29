LC1 = [x for x in range(1,20)]
print(LC1)
print('--------------------------------')

LC2 = [x for x in range(1,20) if x%2 ==0]
print(LC2)
print('--------------------------------')

LC3 = [x if x>2 else x+1 for x in range(1,20)]
print(LC3)
print('--------------------------------')

LC4 = [x for x in range(2,22,2)]
print('Table of no 2 is: ',LC4)