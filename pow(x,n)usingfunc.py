class Python:
    def power(self,x,n):
        if x==0 or x==1 or n==1:
            return x
        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.power(x,-n)
        value = self.power(x,n//2)
        if n%2 ==0:
                return value*value
        return value*value*x

x=int(input("Enter x value :"))
n=int(input("Enter n value :"))
print("The Power(x,n)is :",Python().power(x,n));
