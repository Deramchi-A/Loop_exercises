list_numbers=[12, 75, 150, 180, 145, 525, 50]
new_list=[]
for i in list_numbers:
    
    if i>500:
       break
    elif i>150:
        continue
    elif i%5==0:
        new_list.append(i)
print(new_list)
