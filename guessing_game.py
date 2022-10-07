secret_number = 9
guess_count = 0
guess_limit =3
count =0

while guess_count<guess_limit:
    guess = int(input("guess:"))
    guess_count +=1
    if guess == secret_number:
        print("you won!")
        count+=1
    else:
        #print(f"lose {guess_count}th ")
        print('you lose')
        break
#print(f"you win only {count} time ")
if count  !=0:
    print(f"you won {count} time")
   # print('you lose')
 
    
