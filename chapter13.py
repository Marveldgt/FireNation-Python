'''(b) Write a program that converts ordinary numbers into Roman numerals'''
def to_roman(num):
    dic={1000:'M',900:'MD', 500:'D', 400:'CD',100:'C', 90:'XC',50:'L',40:'XL', 10:'X',9:'IX', 5:'V',4:'IV', 1:'I'}
    m=dict(reversed(list(dic.items())))
    a=list(m.keys())
    i=12
    result=''
    while i>=0:
        div=num//a[i]
        rem=num-(div*a[i])
        if div ==0:
            i-=1
        else:
            result=result + str(m[a[i]]*div)
            if rem==0:
                break
            else:
                num=rem
            i-=1
    print(result)
    
    
num= int(input('enter a number: '))
to_roman(num) 


'''(a) Write a program that converts Roman numerals into ordinary numbers. Here are the conversions: M=1000, D=500, C=100, L=50, X=10, V=5 I=1. Don’t forget about things like IV being 4 and XL being 40'''
def to_roman(roman):
    dic={'M':1000,'CM':900,'D':500,'CD':400, 'C':100, 'L':50,'XL':40, 'X':10,'IX':9, 'V':5,'IV':4, 'I':1}
    a=list(dic.keys())
    i=1
    r=[]
    b= 1
    if len(roman)== 1:
            r.append(dic[roman])
            print(sum(r))
    elif len(roman)==2:   #2-digits roman numeral
            if roman not in a:
                x=dic[roman[b-1]]
                y= dic[roman[b]]
                r.append(x)
                r.append(y)
                print(sum(r))
            else:
                r.append(dic[roman])
                print(sum(r))
    else:
        while i<=len(roman):
            if len(roman)%2==0 and len(roman)!=2: #if no of roman numeral digit is even except 2
                if roman[i-1:i+1] not in a: 
                    d=dic[roman[i-1]]
                    e=dic[roman[i]]
                    r.append(d)
                    r.append(e)
                    i+=2
                    
                else:   
                    k=dic[roman[i-1:i+1]]  
                    r.append(k)
                    i+=2
            else: #if no of digits is odd
                if roman[i-1:i+1]  in a:
                    r.append(dic[roman[i-1:i+1]])
                    r.append(dic[roman[i+1]])
                    i+=3
                else:
                    if roman[i:i+2]  in a:
                        r.append(dic[roman[i:i+2]])
                        r.append(dic[roman[i-1]])
                        i+=3
                    else:
                        r.append(dic[roman[i]])
                        r.append(dic[roman[i-1]])
                        r.append(dic[roman[i+1]])
                        i+=3
            
        print(sum(r))
   
roman= input('enter a roman numeral: ').upper()
to_roman(roman)



'''Write a function called sum_digits that is given an integer num and returns the sum of the digits of num'''

def sum_digits(n):
    s=0
    k=list(n)
    for i in range(len(k)):
        s=s+int(k[i])
    print(f'sum of digits is {s}')
    
    
num=input('enter any integer: ')
sum_digits(num)



'''Write a function called verbose that, given an integer less than 10^15, returns the name of the integer in English. As an example, verbose(123456) should return one hundred twenty-three thousand, four hundred fifty-six'''
dic={10**15:'quadrillion',10**12:'trillion',10**9:'billion',10**6:'million',10**3:'thousand',10**2:'hundred'}
M=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
A=['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninenty','hundred']
def verbose(n):
    i=0
    L= list(dic.keys())
    a=len(L)
    result=''
    while i<=a:
        div=n//L[i]
        rem=n-(L[i]*div)
        if div==0:
            i+=1
        else:
            if 1<=div<= 20:
                h=str(rem)
                if len(h)==2:
                    if len(h)==2 and int(h[0])==1:
                        k= M[div]
                        l=dic[L[i]]
                        j=M[rem]
                        result=result+ ' '+k+' '+l+' '+j
                        break
                    elif len(h)==2 and int(h[0])>=2:
                        k= M[div]
                        l=dic[L[i]]
                        j=A[int(h[0])]
                        m= M[int(h[1])]
                        result=result + ' '+k+' '+l+' '+j+' ' +m
                        break
                elif len(h)>=3:
                        k= M[div]
                        l=dic[L[i]]
                        result=result+k+' '+l
                        n=rem
                        i+=1
                elif rem==0:
                    y=M[div]
                    f=dic[L[i]]
                    result=result+y+' '+f
                    break
            elif 21<=div<=99:
                x=str(div)
                k=A[int(x[0])]
                j=M[int(x[1])]
                l=dic[L[i]]
                result=result+k+'-'+j+' '+l
                n=rem
                i+=1
            elif 100<=div<=999:
                if rem!= 0:
                    x=str(div)
                    k=M[int(x[0])]
                    j=A[int(x[1])]
                    f=M[int(x[2])]
                    l=dic[L[i]]
                    result=result+k+' hundred '+j+' '+f+' '+l+' '
                    n=rem
                    i+=1
                else:
                    x=str(div)
                    k=M[int(x[0])]
                    l=dic[L[i]]
                    result=result+k+' hundred '+l
                    break
    print(result)
                    #break
user=int(input('enter any integer: '))
verbose(user)
