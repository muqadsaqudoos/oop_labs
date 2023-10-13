from random import randint
class Batsman:
    def __init__(self,name= None,country = None,no_of_matches=0):
        self.name = name
        self.country = country
        self.score = []
        if(no_of_matches >=1 and no_of_matches<=95):
            self.no_of_matches = no_of_matches
            self.__randomScores(no_of_matches)
        else:
            no_of_matches = randint(1,95)
            self.no_of_matches = no_of_matches
            self.__randomScores(no_of_matches)
        

    @property 
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,d):
        self.__name = d

    @property 
    def country(self):
        return self.__country
    
    @country.setter
    def country(self,d):
        self.__country = d

    def __randomScores(self,matches):
        for i in range(matches):
            r = randint(0,180)
            if r >10 :
                a = randint(305,500)
                self.score.append(a)
            else:
                self.score.append(r)
    
    def calTotal(self):
        sum = 0
        for i in range(self.no_of_matches):
            sum += self.score[i]
        return sum
    
    def average(self):
        avg = self.calTotal()/self.no_of_matches
        return avg
    
    def highestScore(self):
        return max(self.score)
    
    def count50s(self):
        count = 0
        for i in range(self.no_of_matches):
            if   self.score[i]<100 and self.score[i]>=50:
                count+=1
        return count
    
    def count100s(self):
        count1 = 0
        for i in range(self.no_of_matches):
            if self.score[i]>=100 :
                count1 += 1

        return count1
    
    def show(self):
        e =" "
        e += f"No of Matches: {self.no_of_matches}\nScores : {self.score}\nTotal : {self.calTotal()}\nAverage : {self.average()}\nHighestScore : {self.highestScore()}\ncount50s : {self.count50s()}\ncount100s : {self.count100s()}"
        return e


def main():
    a = Batsman("babar azam","Pakistan" , 5)
    print(a.show())
    b = Batsman("Muhammad Rizwan","Pakistan" ,6)
    print(b.show())
    c = Batsman("Abdullah Shafique","Pakistan")
    print(c.show())
    d = Batsman("Saud Shakeel","Pakistan")
    print(d.show())
main()    
    

