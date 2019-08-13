def sumap( a, d,n) : 
    sum = 0
    j = 0
    while j < n : 
        sum = sum + a 
        a = a + d 
        j = j + 1
    return sum
n = 5
a = 1
d = 0
print (sumap(a, d, n)) 
