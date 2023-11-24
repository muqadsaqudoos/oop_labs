file1 = open("\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\grades.txt","r")
file2 = open("\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\errors.txt","w")
file1.readline()
file1.readline()
x = file1.readlines()

i = 3
for line in x:
    a = line[0:4]
    b = line[43:49]
    c = line[49:52]
    d = line[52:55]
    e = line[55:58]
    b = b.strip()
    c = c.strip()
    d = d.strip()
    e = e.strip()
    list = []
    if a != "BSEF" and a!="BITF" :
        if i not in list:
            file2.write(str(i)+"\n")
            file2.write(line+"\n")
            list.append(i)
    if b == "":
         if i not in list:
            file2.write(str(i)+"\n")
            file2.write(line+"\n")
            list.append(i)
    if c == "" or c=="AB":
        if i not in list:
            file2.write(str(i)+"\n")
            file2.write(line+"\n")
            list.append(i)

    if d == "" or d=="AB":
         if i not in list:
            file2.write(str(i)+"\n")
            file2.write(line+"\n")
            list.append(i)
    if e == "" or e=="AB":
         if i not in list:
            file2.write(str(i)+"\n")
            file2.write(line+"\n")
            list.append(i)
    i+=1

file1.close()
file2.close()