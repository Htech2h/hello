import hello

x = "can you do that?"
y = []
y.append(x.split())

working_list = []
sum = 0
for i in y[0]:
    if len(y[0]) != 0:
        working_list.append(len(i))
        sum += len(i) 
   

to_work = (working_list)
#print( round((sum - to_work[-1]) + (len(to_work)/(to_work[-1]))))
hello.compresion("hello")


