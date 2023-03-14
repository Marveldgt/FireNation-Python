'''(a) Write a program that converts Roman numerals into ordinary numbers. Here are the conversions: M=1000, D=500, C=100, L=50, X=10, V=5 I=1. Don’t forget about things like IV being 4 and XL being 40. (b) Write a program that converts ordinary numbers into Roman numerals'''
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
                    #print(sum(r))
                    i+=2
                    
                else:   #if no of digits is odd
                    k=dic[roman[i-1:i+1]]  
                    r.append(k)
                    i+=2
            else:
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



#bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

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
