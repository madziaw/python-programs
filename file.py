choice = input('Enter 1 to read a file, Enter 2 to write to a file: ')
if choice == '1':
    file_name = input('Enter file name: ')
    file_name = open(file_name,'r')    
    a = file_name.read()
    print(a) 
elif choice == '2':
    file_name = input('Enter file name: ')
    file_name = open(file_name, 'w')
    text = input('Enter text: ')   
    file_name.write(text +'\n')
    file_name.close()
else:
    print('Error! Choose 1 or 2.')
