### Possible U-2 Green assignment and/or practice?
## FOILed again Super Easy Version
## using factored form (Ax + B)(Cx + D)
## foiler() takes A B C D as args and
## return expanded binomial in standard form
## ax^2 + bx + c

##start with helper that performs F.O.I.L
def foiler(A,B,C,D):
    a = str(A*C)
    b = str(B*C + A*D)
    c = str(B*D)
    bin = a + "x^2 + " + b + "x + " + c
    print(bin)

foiler(3,2,3,3)

#Evaluate parses binomial and passes a,b,c,d to foiler
#assume all positve coefficients and '1x' for x
def evaluate(bin):
    abcd = []
    for n in bin:
        if(n in " ()+x"):
            continue
        else:
            abcd.append(n)
    a = int(abcd[0])
    b = int(abcd[1])
    c = int(abcd[2])
    d = int(abcd[3])
    foiler(a,b,c,d)
            
evaluate("(3x + 2)(3x + 3)")
