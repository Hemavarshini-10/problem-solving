num=int(input("enter the number:"))
original_number=num
reverse_number=0
while num>0:
    ld=num%10
    reverse_number=(reverse_number*10)+ld
    num=num//10
print(reverse_number)
