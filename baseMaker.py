# Base-2 maker
## This could be a good unit 4 in class activity after learning bases 
# (or in place of some of the base-changing worksheet)
## Alg: Successively divide by two and store remainder

###Recursive (is this the preferred approach of temp argument?)
def baseX(n, b, out = ""):
    if n == 0:
        print(out)
    else:
        rem = str(n%b)
        baseX(n//b, b, rem + out)

baseX(62,3)


###Iterative
def baseZ(n, b):
    out = ""
    while(n > 0):
        rem = str(n%b)
        out = rem + out
        n = n//b
    print(out)

baseX(139,4)

