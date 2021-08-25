import statistics

listavazia = []
print(listavazia)

listavazia.append(9.5) 
listavazia.append(8.7)
listavazia.append(5.5)  
print(listavazia)

del(listavazia[1])

print(listavazia)

listavazia.insert(1,8.8)
print(listavazia)

listavazia.append(9.7)
print(listavazia)

listavazia[len(listavazia)-1] = 10

media = statistics.mean(listavazia)
print(media)

