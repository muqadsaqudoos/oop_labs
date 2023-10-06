from task_1 import Department
from task_1 import Student


def main():
    deparmentList=[]
    d1 = Department("Computer Science","Dr. Jodat Kamal","CS")
    deparmentList.append(d1)
    d2 = Department("Data Science","Dr. Idress","DS")
    deparmentList.append(d2)
    d3 = Department("Software Enigneering","Dr. Hamna Kaleem","SE")
    deparmentList.append(d3)
    d4 = Department("Information Technology","Dr. Abbas Ali","IT")
    deparmentList.append(d4)
    studentList = []
    s1 = Student("Noman","XXXXXX","1st",3.08,"CS")
    studentList.append(s1)
    s2 = Student("Basit","YYYYYY","2nd",3.08,"SE")
    studentList.append(s2)
    s3 = Student("Nawaz","ZZZZZZ","1st",2.78,"CS")
    studentList.append(s3)
    s4 = Student("Ahmad","XXXXXX","1st",3.38,"IT")
    studentList.append(s4)
    s5 = Student("Qudoos","YYYYYY","2nd",3.38,"DS")
    studentList.append(s5)
    s6 = Student("Ayan","ZZZZZZ","1st",2.82,"IT")
    studentList.append(s6)
    s7 = Student("Ahmad","ZZZZZZ","1st",1.50,"DS")
    studentList.append(s7)
    s8 = Student("Azhar","ZZZZZZ","1st",1.29,"SE")
    studentList.append(s8)
    for i in range(len(deparmentList)):
        print(deparmentList[i])
        for j in range(len(studentList)):
            if (deparmentList[i].ID == studentList[j].departmentId):
                print(studentList[j])
    print("FAIL STUDENTS:")
    for i in range(len(studentList)):
        if studentList[i].cgpa < 1.70:
            print(studentList[i])
    
if __name__ == "__main__":
    main()