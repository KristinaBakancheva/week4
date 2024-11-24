



list_of_profuct = list()


print('')
print('')

list_element =  input('What you want to buy?     ')
while len(list_element) > 1:
    list_of_profuct.append(list_element.capitalize())
    list_element =  input('What else?     ')
print(sorted(list_of_profuct))

print('')
print('')