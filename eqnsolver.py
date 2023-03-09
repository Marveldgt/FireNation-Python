""" calculator that can solves equation of degree 1 in 2 unknowns and 3 unknowns and solve degree 2 equation"""
import numpy as np
import cmath
def solution(unk): #solution to degree 1 equation with 2 and 3 unknowns
    if unk==2:
        x1= int(input('x1= ')); y1=int(input('y1= ')) ; c1= int(input('c1= ')) ; x2= int(input('x2= ')) ; y2= int(input('y2= ' )) ; c2= int(input('c2= '))
        d=np.array([x1,y1,x2,y2]).reshape(2,2)
        d_= np.linalg.inv(d)
        e= np.array([c1,c2]).reshape(2,1)
        f= np.dot(d_,e)
        x,y= f[(0,0)], f[(1,0)]
        print(f'x= {round(x,2)}, y= {round(y,2)}')
    elif unk==3:
        x1= int(input('x1= ')); y1=int(input('y1= ')) ; z1= int(input('z1= ')) ; c1= int(input('c1= ')) ; x2= int(input('x2= ')) ; y2= int(input('y2= ' )) ; z2= int(input('z2= ')) ; c2= int(input('c2= ')); x3= int(input('x3= ')) ; y3= int(input('y3= ' )) ; z3= int(input('z3= ')) ; c3= int(input('c3= '))
        A= np.array([x1,y1,z1,x2,y2,z2,x3,y3,z3]).reshape(3,3)
        A_=np.linalg.inv(A)
        B=np.array([c1,c2,c3]).reshape(3,1)
        B_= np.dot(A_,B)
        X,Y,Z = B_[(0,0)],B_[(1,0)],B_[(2,0)]
        print(f'x= {round(X,2)}, y= {round(Y,2)}, z={round(Z,2)}')         
    else:
        print('wrong input!!! enter 2 or 3')

'''                           hhhh                             '''

def sol_2():  #solution to degree 2
    a = int(input('a= ')); b=int(input('b= ')) ; c= int(input('c= '))
    p= (b**2)- (4*a*c)
    q=(cmath.sqrt(p))
    ans_1= (-b+q)/(2*a)
    ans_2= (-b-q)/(2*a)
    print(f'x= {ans_1} or {ans_2}')

'''                        bbbb                                '''

def eqn(degree):   #defines the degree and unknowns
    if degree==1:
        print('enter number of unknowns (2 or 3)')
        unk= int(input(' '))
        solution(unk)
    elif degree==2:
        sol_2()
    else:
        print('wrong input!!! enter 1 or 2')
        quit()

print('Equation solver  activated\n')
print('enter the degree of the equation (1 or 2)')
degree= int(input(' '))
eqn(degree)
