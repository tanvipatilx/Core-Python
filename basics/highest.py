numbers=[100,20,30,40,90]
highest=0
second_highest=0
for n in numbers:
    if n > highest:
        second_highest=highest
        highest=n
    elif n > second_highest and n!=highest:
        second_highest=n
print("highest number is: ",highest)
print("second highest is: ",second_highest)
