eng=int(input("enter the marks in eng:  "))
math=int(input("enter the marks in math:  "))
beng=int(input("enter the marks in bwng:  "))

total=int(eng+math+beng)

eperc=(((eng)/100)*100)
mperc=(((math)/100)*100)
bperc=(((beng)/100)*100)

totalperc=(((total)/300)*100)

print(total)

print(eperc)
print(mperc)
print(bperc)

print(totalperc)

if(totalperc>=40):
  if(eperc>=33 and mperc>=33 and bperc>=33):
    print("You are passed")
  else:
    print("You are failed")
else:
  print("You are failed")


