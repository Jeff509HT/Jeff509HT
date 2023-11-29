N=int(input("Entrer le nombre de matiere: ")  )
list=[]

for i in range(N):
    note=int(input("Entrer la note: "))
    list.append(note)
    
moy=float(sum(List_note)/kantite_Note)
print("rezilta mwayen se: ",moy)
if (moy>=90):
    print("Coefficient: A")
elif(moy>=80 and moy<90):
    print("Coefficient: B")
elif(moy >=70 and moy<80):
    print("Coefficient: C")
elif(moy >=60 and moy<70):
    print("Coefficient: D")
elif(moy<60):
    print("Coefficient: F")
