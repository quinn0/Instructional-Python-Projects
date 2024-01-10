
#Triangle number warmup 
##Given input, print the first n triangle numbers (starting with 0)
## a1, a2, a3, a4, .... a_n
def tNums(n):
    result = ""
    for i in range(n):
        a_n = str(i*(i+1)//2)
        result += a_n
        if(i < n-1):
            result +=  ", "
    return result

print(tNums(10))




##Synthetic division: 2 Red Points 
## give coefficients of polynomial and root
## temp stores operation
#result stores end coefficients
# returns result as a string
def synthAlg(coeff, root):
    #go through each coeff at a time, update temp as sum of product of prev temp and root with next coeff
    temp = coeff[0]
     ##'bring down' first coefficient'
    result = [str(temp)]    
    for num in coeff[1:]:
        temp = temp*root + num
        result.append(str(temp))
    
    ##writing expression in ax**n + bx**n-1 + ...
    deg = len(result) - 2 ## degree of polynomial (minus remainder and constant term)
    quotient = ""
    for i in range(len(result)):
        ##skip to next degree if 0 coefficient
        if result[i] == "0" or deg < 0:
            deg -= 1
            continue
        elif deg== 1:
            quotient += result[i] + "x + "
        elif deg == 0:
            quotient += result[i]
        else:
            quotient += result[i] + "x^"+ str(deg) + " + "
        deg -= 1
    ##when leading coefficient is 1
    if(quotient[0] == "1"):
        quotient = quotient[1:]
    if int(result[-1]) != 0 :
        return(quotient + " + " + result[-1] + "/" + "(x - "+str(root)+")")
    else:
        return(quotient)

##Test Cases

###Binomial leading coeff != 1
    #(2x+5)(x+3)
    #2x^2 + 11x + 15

test = [2, 11, 15]
root = -3
    #(2x^2 + 11x + 15)/(x+3) = 2x + 5
print(synthAlg(test, root))

###Higher Power

    # x^4 - 3 x^3 + 5 x^2 - 17 x + 6
    #(x - 3) (x^3 + 5 x - 2)
test = [1, -3, 5, -17, 6]
root = 3
    #(x^4 - 3 x^3 + 5 x^2 - 17 x + 6)/(x-3) = x^3 + 5x - 2
print(synthAlg(test, root))

### Remainder in result
    #(x^4 - 5x^3 + 7x^2 - 34x - 1)/(x-5) = x^3 + 7x + 1 + 4/(x-5)
test = [1, -5, 7, -34, -1]
root = 5
print(synthAlg(test, root))

### Gap in terms and remainder in result
    #(2x^4 + 6x^3 + 5x^2 - 44)/(x + 3)
test = [2, 6, 5, 0 , -44] ##0 for missing linear term
root = -3
print(synthAlg(test, root))

