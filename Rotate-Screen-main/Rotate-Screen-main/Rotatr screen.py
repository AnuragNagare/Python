import rotatescreen

screen = rotatescreen.get_primary_display()

message = '''
Enter 1 to rotate up
Enter 2 to rotate down
Enter 3 to rotate left
Enter 4 to rotate right
'''

print(message)

choice = int(input('enter your rotation choice:'))

if choice == 1:
    screen.set_landscape()
elif choice == 2:
    screen.set_landscape_flipped()
elif choice == 3:
    screen.set_portrait_flipped()
elif choice == 4:
    screen.set_portrait()
else:
    print('wrong choice')


