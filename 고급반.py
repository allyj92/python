# a = int(input("입력:"))
# b = int(input("입력:"))

# s = a + b - b**2

# if s >= 0:
#     print(s)
# else:
#     print("음수")

# num = int(input("입력:"))

# if (num%2 == 0) and (num%3 == 0):
#     print("나누어짐")
# else: 
#     print("나누어지지 않음")     

# a = int(input("n1:"))
# b = int(input("n2:"))

# if (a-b)>0 : 
#     print("a>b")
# elif (a-b)<0:
#     print("a<b")   
# else : 
#     print("a=b")    

# a=5
# b=3

# k = input("+,-,*,/ 중 하나를 입력하세요:")

# if k == "+":
#     print(a+b)
# if k == "-" :
#     print(a-b)
# if k == "*" : 
#     print(a*b)
# if k == "/" :
#     print(a/b)                   
# num = [8,7,3,2,9,4,1,6,5]
# print("최대값:",max(num))
# print("최소값:",min(num)) 

# import sys
# maxnum = -sys.maxsize-1
# minnum=sys.maxsize

# for i in range(1,6):
#   print(i,6-i)

# for i in range(10,21):
#     f = (i * 9/5 + 32)
#     print(i,"=",f,"F")    



# def one2n_sum1(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum

# num = int(input("입력:"))

# if num < 0 : 
#     print("입력된 수가 1보다 작습니다.")
# else:
#     print(one2n_sum1(num))
# def m2n_sum(a, b):
#     s = 0   
#     if a > b:
#         k = a
#         a = b
#         b = k
           
#     for i in range(a, b + 1):
#          s += i    
#     return s
    
# n1 = int(input("1:"))    
# n2 = int(input("2:"))   

# result = m2n_sum(n1, n2)
# print("합:", result)



# def pzn(n): 
#     if n > 0:
#         return 1
#     elif n==0:
#         return 0
#     else:
#         return -1

# while True:
#     n = int(input("1:"))
#     if pzn(n) == 1 :
#         print("양수")
#     elif pzn(n) == -1 :
#         print("음수")
#     else :
#         break

# print("0")

# num = int(input("입력:"))
# if num < 100 :
#     print(num*0.9)
# else:
#     print(num*1.1)    

# a = int(input("정수1:"))
# b = int(input("정수2:"))

# s = a+b-b**2

# if (s >=0):
#     print(s)
# else :
#     print("음수")    

# num = int(input("정수:"))

# if (num %2 == 0) and (num % 3 == 0):
#     print("나누어짐")
# else:
#     print("나누어지지않음")

# a = int(input("1:"))
# b = int(input("2:"))

# s = a-b

# if s > 0:
#     print("a>b")
# elif s < 0 :
#     print("a<b")
# elif s == 0:
#     print("a=b")
# else: 
#     print("정수를 입력하세요")    

# a=5
# b=3
# s = input("+,-,*,/ 중 하나를 입력하세요:")  
# if s == "+":
#     print(a+b) 
# elif s == "-":
#     print(a-b)
# elif s == "*":
#     print(a*b)
# elif s == "/":
#     print(a/b)
# else :
#     print("올바른 연산자를 입력하세요.")    


# for i in ["국어","영어","수학","과학","한국사"]:
#      print(i,end= " ")

# name = ["홍길동","임꺽정"]
# sub = ["국어","영어","수학"]

# for i in name:
#     for j in sub:
#         print(i,j)
# sum=0
# for i in range (1,101):
#      sum+=i
# print(sum)

# sum1=0
# sum2=0
# for i in range(1,101):
#     if i%2 == 1 :
#         sum1+=i
     
#     else:
#         sum2+=i   
# print(sum1,sum2)

# def print_python():
#     print("파이썬")

# print_python()  

# def welcome():
#     for i in range(3):
#        print("환영합니다")

# welcome()     

# def welcome(name):
#     print("환영합니다",name,"님")

# n=input("이름:")
# welcome(n)    

# def print_str(s,n):
#     for i in range(n):
#         print(s)

# s = input("문자열:") 
# number = int(input("횟수:"))

# print_str(s,number)

# def dispch(a,b):
#     for i in range(b):
#         print(a)

# aa=input("문자:")
# bb=int(input("횟수:"))

# dispch(aa,bb)

# def maxnum(m,n):
#     if m>=n:
#         maxmn = m 
#     else : 
#         maxmn = n    
#     return maxmn

# aa = int(input("1:"))    
# bb = int(input("2:"))  
# print("큰 수=",maxnum(aa,bb)) 

# def minnum(m,n):
#     if m<=n:
#         maxmn = m
#     else:
#         maxmn = n
#     return maxmn

# aa = int(input("1:"))    
# bb = int(input("2:"))  
# print("작은수=",minnum(aa,bb))       

# def pow_xy(x,y) :
#     return x**y
 
# print(3*pow_xy(2,4)+5)

 
# dic = {'name':'pey','phone':"010-9999-1234", 'birthday':'1118'}
# print(dic)

# a={1:'hi'}
# print(a[1])
# a[2]='v'
# print(a)
# a[3]= 'c'
# print(a)
# a={'a':[1,2,3,4]}
# print(a)
# a = {'name':'pey','phone':"010-9999-1234", 'birthday':'1118'}
# print(a.keys())

# for k in a.keys():
#     print(k)

# print(a.values())    

# #a.clear()

# print(a.get('name'))

# import turtle
# turtle.speed(1)

# turtle.shape("turtle")
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)

# for i in range(0,4):
#     turtle.shape("turtle")
#     turtle.right(90)
#     turtle.forward(100)

# import enum
# import turtle as t
# t.speed(1)

# #1
# turtle.shape("turtle")
# turtle.forward(100)

# #2
# turtle.speed(1)
# turtle.shape("arrow")
# turtle.left(180)
# turtle.forward(50)
# turtle.backward(30)

# #3
# turtle.shape("turtle")
# turtle.circle(100)

#4
# t.shape("turtle")
# for i in range(3):
#     t.left(120)
#     t.forward(100)

# #5
# t.shape("turtle")
# t.circle(100)    
# for i in range(3):
#     t.left(120)
#     t.forward(100)

# #6
# t.shape("turtle")
# for i in range(6):
    
#     t.forward(100)
#     t.left(60)

# t.circle(100)

# t.speed(1)
# t.shape("turtle")
# t.forward(40)
# t.left(90)
# t.forward(80)
# t.right(90)
# t.forward(40)
# t.right(90)
# t.forward(80)
# t.left(90)
# t.forward(30)
# t.left(90)
# t.forward(80)
# t.right(90)
# t.forward(90)
# t.right(90)
# t.forward(80)
# t.left(90)
# t.forward(40)

# t.shape("turtle")
# t.speed(1)
# t.forward(100)
# t.up()
# t.goto(0,-50)
# t.down()
# t.forward(100)
# t.up()
# t.goto(0,-100)
# t.down()
# t.forward(100)

# t.speed(1)
# t.shape("turtle")
# t.speed(1)
# t.forward(100)
# t.up()
# t.goto(0,50)
# t.down()
# t.forward(100)
# t.up()
# t.goto(0,100)
# t.down()
# t.forward(100)
    
    
# len = int(input("길이:"))

# t.speed(1)
# t.shape("turtle")
# t.forward(len)

# side = int(input("정수:"))
# for i in range(side):
#     t.left(120)
#     t.forward(side)

# t.speed(1)
# radius = int(input("반지름:"))
# t.circle(radius, steps=4)

# distance = int(input("거리:"))
# for i in range(4):
#     t.shape("turtle")
#     t.speed(1)
#     t.forward(distance)
#     t.right(90)

# for i in range (3):
#     t.shape("turtle")
#     t.speed(1)
#     t.circle(50)
#     t.right(120)

# for i in range (3):
#     t.circle(50)
#     t.up()
#     t.forward(50)
#     t.down()



# def rectangle_draw(col,row):
#     for i in range(2):
#         t.forward(col)
#         t.right(90)
#         t.forward(row)
#         t.right(90)  
#     print(f'가로{col} 세로{row}인 사각형의 넓이 = {col*row}')        

# width = int(input("가로:"))
# height = int(input("세로:"))
# rectangle_draw(width,height)

# def circle_draw(radius):
#     t.circle(radius)
#     print(f'반지름 {radius}인 원의 넓이 = {radius*radius*3.141592}')

# r = int(input("반지름:"))
# circle_draw(r)


# comp_dict = {'A':'T','T':'A','C':'G','G':'C'}
# print(len(comp_dict))
# print(comp_dict.keys())
# print(comp_dict.values())

# print(comp_dict['T'])

# digit = {1:'일',2:'이',3:'삼'}
# print(len(digit))
# print(digit.keys())
# print(digit.values())


# fruit = {'사과':100, '바나나':50, '수박':1000}
# print(len(fruit))
# print(fruit.keys())
# print(fruit.values())

# import turtle as t

# def write_xy(x,y):
#     t.goto(x,y)
#     t.stamp()
#     t.write(f"x:{x},y:{y}")

# def screen_clear(x,y):
#     t.goto(x,y)
#     t.clear()

# t.setup(600,600)
# s = t.Screen()
# t.penup()

# s.onscreenclick(write_xy,1)
# s.onscreenclick(screen_clear,3)
# s.listen()

# items = {"라면":650,"우유":1100, "콜라":1200,"캔커피":500,"과자":700}
# sum=0
# while True:
#     it = input("제품명:")
#     if it =="":
#         break  
#     if items[it] > 1100:
#         sum+=items[it]
#         print(f'[{it}:{items[it]}]')
        
#     else:
#         print(it, "는 미등록 제품입니다")
# print(sum) 



# import turtle as t


# def write_xyleft(x,y):
#     t.goto(x,y)
#     t.write(f"{x}:,{y} - 마우스 왼쪽 버튼 클릭")

# def write_xyright(x,y):
#     t.goto(x,y)
#     t.write(f"{x}:,{y} - 마우스 오른쪽 버튼 클릭")

# t.setup(600,600)
# s = t.Screen()
# t.penup()

# s.onscreenclick(write_xyleft,1)
# s.onscreenclick(write_xyright,3)
# s.listen()


# import turtle as t


# def write_xyleft(x,y):
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.circle(20)
    

# def write_xyright(x,y):
#     t.penup()
#     t.pendown()
#     t.clear()
   

# t.setup(600,600)
# s = t.Screen()
# t.penup()

# s.onscreenclick(write_xyleft,1)
# s.onscreenclick(write_xyright,3)

# t.done()
# s.listen()

# import math  as t

# num = float(input("실수:"))

# print(t.ceil(num))
# print(t.floor(num))
# print(t.trunc(num))

# import math as t

# num = int(input("num:"))
# print(t.sqrt(num))


# def circle_area(r):
#   print(r*r*3.141592)

# num = int(input("반지름:"))
# circle_area(num)  

# import turtle as t

# def rectangle_draw(radius):
     
#      t.circle(radius)

# num = int(input("반지름:"))
# rectangle_draw(num)

# t = {"1":8, "2":6,"3":10,"4":13}

# for i in t:
#     print('#'*t[i])

# a = {"공책":325,"연필":427,"지우개":125,"복사지":510}

# b = int(input("제고수:"))


# for i in a:
#    if(b>a[i]):
#       print(a[i])

# nu = {}

# while True:
#     eng = input("영어 단어 : ")
#     kor = input("국어 단어 : ")
    
#     if eng=="" and kor =="" :
#         break
# print({eng:kor})   
    
# 

# 금액을 금액보다 작은 수 중 가장 큰 수로 나눈것

# money = int(input("금액:"))
# a = {1:50000,2:10000,3:5000,4:1000,5:500,6:100,7:50,8:10,9:5,10:1}
# for i in a:
#     if money > i :
#         print(max(i))


# import turtle
# import math

# # 터틀 그래픽 창을 엽니다
# 화면 = turtle.Screen()

# # 터틀 객체를 생성합니다
# t = turtle.Turtle()

# # 원을 그리는데 필요한 변수 설정
# 반지름 = int(input("반지름:"))  # 원의 반지름
# 각도 = 0

# t.penup()
# # 원을 그리기 시작합니다
# while 각도 <= 360:
#     라디안 = math.radians(각도)
#     x = 반지름 * math.cos(라디안)
#     y = 반지름 * math.sin(라디안)
#     t.goto(x, y)
#     각도 += 1
# print(반지름)   

# t.pendown()
# 그림 그리기를 종료합니다


# turtle.done()

# import turtle

# screen = turtle.Screen()
# t = turtle.Turtle()
# r = int(input("반지름을 입력하세요: "))
# t.circle(r)  
# turtle.done()

# str1 = 'Text'
# str2 = "String"
# str3 = """Text
# String  
# """

# str4 = "Text's string"
# str5 = 'Text "in" string'
# print(str1)
# print(str2)
# print(str3)
# print(str4)

# st = "Text String"
# print(st[0], st[1], st[len(st)-1])
# for i in range(len(st)):
#     print(st[i],end=" ")
# print("")
# print(st[len(st)])    

# st = "Text String"

# if 'x' in st :
#     print("Included")
# else : 
#     print("Not included")
# st1="123"
# st2 = 3.546   
# print(st1,st2)
# st3 = st.replace('S','s')     
# print(st3)
# st4 = "TextString"
# print(st.upper())
# print(st.lower())
# print(st.isdigit(), st4.isdigit(), st1.isdigit()) 
# print(st.isalpha(),st4.isalpha(),st1.isalpha())
# print(st.isalnum(),st4.isalnum(),st1.isalnum())
  
# nm = input("이름:")  
# st2 = nm[0]+nm[-1] 
# print(st2)   

# # 문자열을 입력받기
# st = input("입력:")

# # 만약 문자로만 구성된경우 모든문자를 대문자로 변경


# if st.isalpha():
#     #모든문자를 대문자로 변경 
   
#       st1=  st.upper()
#       print(st1)
# # 만약 숫자로만 구성된 경우 
# if st.isdigit():
#         # 문자열을 숫자로 변경한후+1
#         print(int(st)+1)

# 주민등록번호 형식의 앞 6자리 문자열을 입력받기        

# num = input("주민등록번호 앞자리를 입력하세요: ")

# if int(num[4:6]) >= 1 and int(num[4:6]) <= 12:
#     if int(num[2:4]) >= 1 and int(num[2:4]) <= 31:
#         # 주민등록번호의 7번째 숫자 입력
#         num1 = int(input("주민등록번호의 7번째 숫자를 입력하세요: "))
#         if num1 == 1:
#             print("남성")
#         elif num1 == 2:
#             print("여성")
#         else:
#             print("주민등록번호의 성별 형식이 올바르지 않습니다.")
#     else:
#         print("주민등록번호의 월 형식이 올바르지 않습니다.")
# else:
#     print("주민등록번호의 일자 형식이 올바르지 않습니다.")
       
        
def isbn_check(isbn):
    s = 0
    for i in range(0, 12):
        if (i + 1) % 2 == 1:
            s = s + int(isbn[i]) * 1
        else:
            s = s + int(isbn[i]) * 3
    t = s % 10
    chk = (10 - t) % 10
    print(f"USBN 1~12 digit check mark value: {chk}")

    if chk == int(isbn[12]):
        rst = 1
    else:
        rst = 0
    return rst

isbn = input("ISBN 13 자리 숫자 (하이픈 제외): ")
print(f"ISBN 합계: {isbn}")

if len(isbn) == 13:
    rst = isbn_check(isbn)
    if rst == 1:
        print("검증되었습니다.")
    else:
        print("검증되지 않았습니다.")
else:
    print("ISBN 코드를 입력할 때 하이픈을 제외한 13 자리를 입력하세요.")
  
