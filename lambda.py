numb=eval(input("Enter The Number:"))
x=lambda y:y+25
def lamb(z):
    y = lambda x:x+z
    return y
func_lamb= lamb(25)
print(func_lamb(numb))