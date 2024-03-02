human=['hand','brain','lag','blood']
print(human)
print(human[0])
print(human[3])
print(human[1].title())
print(human[2].upper())
print(human[-1])
print(human.insert(0,'body'))
human.insert(0,'ear')
print(human)
del human[1]
print(human)
human=human.pop(0)
print(human)
len(human)
for human in human:
    print(human)
list=['apple','samsung','intel']
for i in list:
    
    print(i.upper())
for i in range(1,6):
    print(i)    
list=[1,2,23,4,5,-1,0]
print(min(list))
print(max(list))
print(sum(list))
numbers=[i*2 for i in range(1,11)]
print(numbers)    
list=[1,2,3,4]
print(list[0:2])
print(list[:3])
for i in list[0:4]:
    print(i)
mylist=list[:]
print(mylist)
mylist.append(0)
print(mylist)
mylist.insert(0,4)
print(mylist)
dimenions=(200,300)
print(dimenions[0])
print(dimenions[1])
for i in dimenions:
    print(i)