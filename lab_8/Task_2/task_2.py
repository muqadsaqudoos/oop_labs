file1 = open("\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\Task_2\grades2.txt","r+")
file2 = open("\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\Task_2\errors2.txt","r")
file2.readline()
file2.readline()
s = file2.readline()
while s != "":
    lineno = int(s)
    s = file2.readline()   
    file1.seek((lineno-1)*59)
    file1.writelines(s)
    s = file2.readline()

file1.close()
file2.close()