file1 = open("D:\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\Task_1\grades.txt","r")
file2 = open("D:\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\Task_1\errors.txt","w")
a = file1.readline()
file2.writelines(a)
b = file1.readline()
file2.writelines(b)
error = 0
lineno = 3
c = file1.readline()
while c!="":
    roll_no = c[0:10]
    name = c[10:41]
    crs = c[42:48]
    md = c[49:51]
    ss = c[52:54]
    fn = c[55:57]
    if len(c)!=58:
        error += 1 
        file2.writelines(str(lineno)+"\n")
        file2.writelines(str(c))
    elif (len(roll_no.strip())!=10):
        error += 1 
        file2.writelines(str(lineno)+"\n")
        file2.writelines(str(c))
    elif crs.strip()!= "PF" and crs.strip()!= "ITC" and crs.strip()!= "DLD":
        error += 1 
        file2.writelines(str(lineno)+"\n")
        file2.writelines(str(c))
    elif not(md[0]>='0' and md[0]<='9' and md[1]>='0' and md[1]<='9'):
        error += 1 
        file2.writelines(str(lineno)+"\n")
        file2.writelines(str(c))
    elif not(ss[0]>='0' and ss[0]<='9' and ss[1]>='0' and ss[1]<='9'):
        error += 1 
        file2.writelines(str(lineno)+"\n")
        file2.writelines(str(c))
    elif not(fn[0]>='0' and fn[0]<='9' and fn[1]>='0' and fn[1]<='9'):
        error += 1 
        file2.writelines(str(lineno)+"\n")
        file2.writelines(str(c))
    lineno += 1
    c = file1.readline()
file1.close()
file2.close()