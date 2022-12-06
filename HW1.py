a='this is my laptop. i am hanieh an i love python!'
print(a)

num_k = a.count(' ') + 1
num_h = len(a) - a.count(' ') - a.count(',') - a.count('!')
num_j = a.count('.')+ a.count('?')+a.count('!') + a.count(';')
a = a.replace('p','r')

print(num_k)
print(num_h)
print(num_j)
print(a)
