file1 = open("\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\grades1.txt","r")
file2 = open("\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\error1.txt","r")
x = file1.readlines()
file1.close()
file1 = open("\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\grades1.txt","w")
for i in range(5):

    a = int(file2.readline())
    c = file2.readline()
    x[a-1] = c


for line in x:
    file1.write(line)
file1.close()
file2.close()
