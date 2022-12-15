
color = ""

while color != 'quit':


    color = input('Enter "green", "yellow", "red": ').lower()
print(f'The user entered {color}')

if color == 'green':
    print('go!')
elif color == 'yellow':
    print('slow down!')
elif color == 'red':
    print('STOP!')
else:
    print('bogus')
