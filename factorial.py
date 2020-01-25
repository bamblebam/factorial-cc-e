tcase=int(input())
for case in range(tcase):
  num=int(input())
  rev_counter=[]
  counter=1
  counter2=0
  for i in range(1,num+1):
    counter=counter*i
  counter=list(str(counter))
  
  for j in range(len(counter)):
    rev_counter.append(counter[len(counter)-1-j])

  t=len(counter)

  s=[str(k) for k in rev_counter]
  new=int("".join(rev_counter))
  new=str(new)

  x=len(new)
  z=t-x

  print(z)
