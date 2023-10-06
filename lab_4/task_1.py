class Department:
    def __init__(self,name,chairman,ID):
        self.name = name
        self.chairman = chairman
        self.ID = ID


    def __str__(self):
        return f'Department :{self.ID},{self.name},{self.chairman}\nRoll No\t\tName\t\tSemester\t\tCGPA'

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,d):
        self.__name = d
        return self.__name
    
    @property 
    def chairman(self):
        return self.__chairman
    
    @chairman.setter
    def chairman(self,d):
        self.__chairman = d
        return self.__chairman
    
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self,d):
        self.__ID =d
        return self.__ID

class Student:
    def __init__(self,name,rollNo,semester,cgpa,departmentId):
        self.name = name
        self.rollNo = rollNo
        self.semester = semester
        self.cgpa = cgpa
        self.departmentId = departmentId

    def __str__(self):
        return f'{self.rollNo}\t\t{self.name}\t\t{self.semester}\t\t{self.cgpa}'

    @property
    def name(self):
        return  self.__name

    @name.setter
    def name(self,d):
        self.__name = d
        return self.__name
    
    @property
    def rollNo(self):
        return  self.__rollNo

    @rollNo.setter
    def rollNo(self,d):
        self.__rollNo = d
        return self.__rollNo
    
    @property
    def cgpa(self):
        return  self.__cgpa

    @cgpa.setter
    def cgpa(self,d):
        self.__cgpa = d
        return self.__cgpa
    
    @property
    def semester(self):
        return  self.__semester

    @semester.setter
    def semester(self,d):
        self.__semester = d
        return self.__semester
    
    @property
    def departmentId(self):
        return  self.__departmentId

    @departmentId.setter
    def departmentId(self,d):
        self.__departmentId = d
        return self.__departmentId
    

    





