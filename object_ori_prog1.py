'''Write aclass called Investment with fields called principal and interest. The constructor should set the values of those fields. There should be a method called value_after that returns the value of the investment after n years. The formula for this is p(1+ i)^n, where p is the principal, and i is the interest rate. It should also use the special method __str__ so that printing the object will result in something like below: Principal- $1000.00, Interest rate- 5.12%'''

class Investment:
    def __init__(self,p,i,n):
        self.p=p
        self.i=i
        self.n=n
        
    def value_after(self):
        return  f'Tota amount is {round(self.p*((1+(self.i/100))**self.n),2)}'
        
        
        
    def __str__(self):
        return 'principal - ${} , interest rate - {}%'.format(self.p,self.i)
        
        
        
A= Investment(1000,1,3)
print(A.__str__())
print()
print(A.value_after())

'''Write a class called Product. The class should have fields called name, amount, and price, holding the product’s name, the number of items of that product in stock, and the regular price of the product. There should be a method get_price that receives the number of items to be bought and returns the cost of buying that many items, where the regular price is charged for orders of less than 10 items, a 10% discount is applied for orders of between 10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should also be a method called make_purchase that receives the number of items to be bought and decreases amount by that much'''
class Product:
    def __init__(self,n,a,p): #a is amount in stock, p is price , n is name
        self.n=n
        self.a=a
        self.p=p
        
    def get_price(self,b):  #b is amount to be bought
        self.b=b
        if self.b<10:
            return f'The cost of {self.b} {self.n} is ${self.b*self.p}'
        elif 10<=self.b<=99:
            return f'The cost of {self.b} {self.n} is ${self.b*(self.p-(0.1*self.p))}'
        else:
           return f'The cost of {self.b} {self.n} is ${self.b*(self.p-(0.2*self.p))}'
           
    def make_purchase(self,b):
           self.b=b
           self.a= self.a - self.b
           return f'Amount of {self.n} remaining is in stock is {self.a}'
           
e=Product('cheese',1000,40)
print(e.get_price(500))
print(e.make_purchase(500))

'''Write a class called Password_manager. The class should have a list called old_passwords that holds all of the user’s past passwords. The last item of the list is the user’s current password. There should be a method called get_password that returns the current password and a method called set_password that sets the user’s password. The set_password method should only change the password if the attempted password is different from all the user’s past passwords. Finally, create a method called is_correct that receives a string and returns a boolean True or False depending on whether the string is equal to the current password or not'''

class Password_manager:
    def __init__(self,l):
        self.l=l
    def get_password(self):
        return f'Your current password is {self.l[-1]}'
        
    def set_password(self,n):
        self.n=n
        for i in self.l:
            if self.n !=i:
                self.l[-1]=self.n
                return self.l
                
                
    def is_correct(self):
        self.h= input('enter a string')
        if self.h == self.l[-1]:
            return True
        return False
        
k=['oluwaseye','douy7','fant6','olusunmade20']
e=Password_manager(k)
print(e.get_password())
print()
f=input('enter a password: ')
print(e.set_password(f))
print()
print(e.is_correct())

'''Write a class called Time whose only field is a time in seconds. It should have a method called convert_to_minutes that returns a string of minutes and seconds formatted as in the following example: if seconds is 230, the method should return '5:50'. It should also have a method called convert_to_hours that returns a string of hours, minutes, and seconds formatted analogously to the previous method'''

class Time:
    def __init__(self, s):
        self.s=s
    
    def convert_to_minutes(self):
        return f'{self.s//60} : {self.s%60}'
        
    def convert_to_hour(self):
       if self.s>=3600:
           return f'{self.s//3600} ; {(self.s- (self.s//3600))//60} : {self.s%60}'
       return f'0 : {self.s//60} : {self.s%60}'

s= int(input('enter time in seconds: '))       
t= Time(s)
print(t.convert_to_minutes())
print(t.convert_to_hour())

