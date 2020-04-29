import random
import numpy as np

random.seed(17)

class Agent:
    def __init__(self,type,n):
        self.name = type
        self.estop = int(n*(1/np.exp(1)))
        self.sqrtstop = int(np.ceil(np.sqrt(n)))

    def act(self,step,hist,curval):
        if self.name =='random':
            action = random.getrandbits(1)
        elif self.name == 'E':
            if step < self.estop :
                action = 1
            else :
                if curval >= max(hist,default=42):
                    action = 0
                else :
                    action = 1

        elif self.name == 'sqrt':
            if step < self.sqrtstop :
                action = 1
            else :
                if curval >= max(hist,default=42):
                    action = 0
                else :
                    action = 1

        else :
            action = 1

        return action


class Game:
    def __init__(self,agent,score,n=10,prnt=False,seed=17):

        self.n = n
        self.agent = agent
        self.prnt = prnt
        self.seed = seed
        self.name = "Googol"
        self.result = 'none'
        self.reward = 0
        self.selected = 0
        self.score = score


    def get_result(self):
        return self.result

    def playmove(self,step,hist,curval):
        return self.agent.act(step,hist,curval)

    def updatescore(self,value):
        if value == 1:
            self.score.wins += 1
        else :
            self.score.loss += 1

    def playgame(self):
        slips = [random.randrange(1, self.n*10) for _ in range(self.n)]
        for i in range(1, self.n + 1):
            if i == self.n :
                act = 0
            else :
                act = self.playmove(i,slips[:i-1],slips[i-1])
            if act == 0:
                if slips[i - 1] == max(slips):
                    # if (all (Slips[i-1] >= x for x in Slips)):
                    #you won
                    self.result = 1
                    self.updatescore(1)
                    break
                else:
                    #you lost
                    self.result = 0
                    self.updatescore(0)
                    break

        return self.result


class Score:
    def __init__(self,wins=0,loss=0):
        self.wins = wins
        self.loss = loss

    def retscore(self):
        return self.wins,self.loss

    def prntscore(self):
        print("wins: ",self.wins," losses: ",self.loss ,"total: ", self.wins+self.loss)

def prntsco(a,b):
    print("wins: ", a, " losses: ", b, "total: ", a + b)

