import operator

#from goto import goto , label
oper={'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
l#abel:retry
#try :
 num = list(map(int, input().rstrip().split())) 
 a=num[0]
 b=num[1]
#except:
 #goto:retry

print('enter \n+ for add\n- for minus\n* for multiplication \n/ for divide\n')
select=str(input())
print(oper[select](a,b))
#hello bro