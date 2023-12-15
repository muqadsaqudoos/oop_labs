l = ['a', 's', 'd', 'l', 'e', 'q']
print("Select options from the following menu\na) ADD\tb) Search\tc) Delete\td) List All\te) Edit\tq) Quit")
a = input("Enter: ")
while a not in l:
    print("Select options from the following menu\na) ADD\tb) Search\tc) Delete\td) List All\te) Edit\tq) Quit")
    a = input("Enter: ")


if a == "a":
    file = open('D:\Muqadsa Qudoos\semester 2\oop\oop labs\lab_10\courses.txt','r+')
    b = input("Enter code:")
    file.write(b.ljust(8))
    b = input("Enter title: ")
    file.write(b.ljust(40))
    b = input("Enter credit_hours: ")
    file.write(b.ljust(13))
    b = input("Enter default_semester: ")
    file.write(b.ljust(17))
    b = input("Enter type: ")
    file.write(b.ljust(9))
    print("\n")
    file.close()
elif a == "s":
    file = open('D:\Muqadsa Qudoos\semester 2\oop\oop labs\lab_10\courses.txt','r+')
    list = file.readlines()
    code = input("Enter code to be search:")
    for line in list:
        if line[0:9] == code:
            print(line)
elif a == "d":
    file = open('D:\Muqadsa Qudoos\semester 2\oop\oop labs\lab_10\courses.txt','r+')
    line = int(input())
    file.seek((line-1)*88)
    file.write('$')
    file.close()

elif a =="l":
    file = open('D:\Muqadsa Qudoos\semester 2\oop\oop labs\lab_10\courses.txt','r')
    list = file.readlines()
    for line in list:
        print(line)

elif a == "e":
    file = open('D:\Muqadsa Qudoos\semester 2\oop\oop labs\lab_10\courses.txt','r+')
    a = int(input("Enter line to be edit"))
    file.seek(a)
    b = input("Enter code: ")
    file.write(b)
    b = input("Title: ")
    file.write(b)
    b = input("credit_hours: ")
    file.write(b)
    b = input("default_semester: ")
    file.write(b)
    b = input("Type: ")
    file.write(b)
    file.close()
    

else:
    print("Menu quit")
