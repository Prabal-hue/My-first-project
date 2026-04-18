#Tuples Basics 

myTuple=(78,90,75)
StudentTuple=("Prabal", "Niraj", "Ishaan")
print(len(myTuple))

print(StudentTuple[2])
#StudentTuple[1]="Shivam" Tuples are IMMUTABLE/ Cant change 

#Empty Tuples
emptytuple=()
singletuple=(1,) #If asked to write a single tuple then add a , or els it become int 
print(type(emptytuple))
print(type(StudentTuple))
print(type(singletuple))
print(StudentTuple.index("Prabal"))
print(StudentTuple.count("Prabal"))