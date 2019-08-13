def sumap( a, d,n) : 
    sum = 0
    j = 0
    while j < n : 
        sum = sum + a 
        a = a + d 
        j = j + 1
    return sum
n = 3
a = 1
d = 1
print (sumap(a, d, n)) 
