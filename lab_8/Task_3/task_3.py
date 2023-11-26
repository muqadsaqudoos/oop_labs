def result(file,degree):
    a = file.readline()
    b = file.readline()
    print(f"Degree : {degree}")
    print("Sr.No. Roll No.   Student Name                   ITC  PF DLD Total %age Grade")
    print("====== ========== ============================== === === === ===== ==== =====")
    count = 1
    ict_avg = 0
    pf_avg = 0
    dld_avg = 0
    total_avg = 0
    student_count = 0
    for i in range(9):  
        line1 = file.readline()
        line2 = file.readline()
        line3 = file.readline()

        roll_no = line1[0:10]
        name = line1[10:41]

        ict_marks = [int(line1[49:51]), int(line1[52:54]), int(line1[55:57])]
        pf_marks = [int(line2[49:51]), int(line2[52:54]), int(line2[55:57])]
        dld_marks = [int(line3[49:51]), int(line3[52:54]), int(line3[55:57])]
        total_marks = sum(ict_marks) + sum(pf_marks) + sum(dld_marks)
        percentage = (total_marks / 300) * 100

        if percentage >= 85:
            grade = "A"
        elif 80 <= percentage < 85:
            grade = "A-"
        elif 75 <= percentage < 80:
            grade = "B+"
        elif 70 <= percentage < 75:
            grade = "B"
        elif 65 <= percentage < 70:
            grade = "B-"
        elif 61 <= percentage < 65:
            grade = "C+"
        elif 58 <= percentage < 61:
            grade = "C"
        elif 55 <= percentage < 58:
            grade = "C-"
        elif 50 <= percentage < 55:
            grade = "D"
        else:
            grade = "F"

        if degree in roll_no:
            student_count+=1
            print(f"    {count}  {roll_no} {name} {sum(ict_marks)} "
                f" {sum(pf_marks)}  {sum(dld_marks)} "
                f"  {total_marks} {percentage:.1f}   {grade}  ")
            ict_avg += sum(ict_marks)
            pf_avg += sum(pf_marks)
            dld_avg += sum(dld_marks)
            total_avg += total_marks
            count += 1
    print("                                                  =========================")
    print(f"                              {degree} Degree Average  {ict_avg//student_count}  {pf_avg//student_count}  {dld_avg//student_count}   {total_avg//student_count}")


file = open("\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\Task_3\grades3.txt","r")
degree1 = result(file,"BIT")
file.close()
file = open("\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\Task_3\grades3.txt","r")
degree2 = result(file,"BSE")
file.close()
file = open("\Muqadsa Qudoos\semester 2\oop\oop labs\lab_8\Task_3\grades3.txt","r")
degree3 = result(file,"BCS")
file.close()
