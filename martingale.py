""""""  		  	   		  		 		  		  		    	 		 		   		 		  
"""Assess a betting strategy.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  		 		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  		 		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  		 		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  		 		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  		 		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  		 		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  		 		  		  		    	 		 		   		 		  
or edited.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  		 		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  		 		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  		 		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		  	   		  		 		  		  		    	 		 		   		 		  
GT User ID: tb34 (replace with your User ID)  		  	   		  		 		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		  		 		  		  		    	 		 		   		 		  
"""  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  		 		  		  		    	 		 		   		 		  
import matplotlib.pyplot as plt	  	  
import pandas as pd 	
from pandas import DataFrame	  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def author():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT username of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: str  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return "tb34"  # replace tb34 with your Georgia Tech username.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def gtid():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The GT ID of the student  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: int  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    return 900897987  # replace with your GT ID number  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def get_spin_result(win_prob):  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Given a win probability between 0 and 1, the function returns whether the probability will result in a win.  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
    :param win_prob: The probability of winning  		  	   		  		 		  		  		    	 		 		   		 		  
    :type win_prob: float  		  	   		  		 		  		  		    	 		 		   		 		  
    :return: The result of the spin.  		  	   		  		 		  		  		    	 		 		   		 		  
    :rtype: bool  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  
   

    result = False  		  	   		  		 		  		  		    	 		 		   		 		  
    if np.random.random() <= win_prob:  		  	   		  		 		  		  		    	 		 		   		 		  
        result = True  		  	   		  		 		  		  		    	 		 		   		 		  
    return result  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
  		  	   		  		 		  		  		    	 		 		   		 		  
def test_code():  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    Method to test your code  		  	   		  		 		  		  		    	 		 		   		 		  
    """  		  	   		  		 		  		  		    	 		 		   		 		  
    win_prob = 0.60  # set appropriately to the probability of a win  		  	   		  		 		  		  		    	 		 		   		 		  
    np.random.seed(gtid())  # do this only once  		  	   		  		 		  		  		    	 		 		   		 		  
    print(get_spin_result(win_prob))  # test the roulette spin  
    print(simulator_exp1(win_prob))
    print(simulator_exp2(win_prob))
    

    # add your code here to implement the experiments  		  	 
def plot_exp_1(res):
### plot_1
    df = pd.DataFrame(res)
    df.plot()
    axis = [0,300,-256,100]
    plt.axis(axis)
    plt.title("Figure 1 10 trials with unlimited bankroll")
    plt.xlabel("Trial Number")
    plt.ylabel("winnings")
    index = 10
    for i in range(index):
        cur = simulator_exp1(.60)
        plt.plot(cur)
    plt.savefig("figure1.png")
    plt.clf()


### plot_2():
   
    plt.axis(axis)
    plt.title("Figure 1 10 trials with unlimited bankroll")
    plt.xlabel("Trial Number")
    plt.ylabel("winnings")
    index = 1000
    zeros = np.full((1000,1001), 0)
    for i in range(index):
        cur = simulator_exp1(.60)

        zeros[i] = cur
    mean  = np.mean(zeros, axis = 0)
    std = np.std(zeros, axis = 0)
    added = mean + std
    subtracted = mean - std
    
    
    np.mean(zeros) 
    df = pd.DataFrame(mean)
    df1 = pd.DataFrame(added)
    df2 = pd.DataFrame(subtracted)

    #df.plot()
    axis = [0,300,-256,100]
    plt.axis(axis)
    plt.title("Figure2 - mean of 1000 trials with unlimited bankroll")
    plt.xlabel("Trials")
    plt.ylabel("winnings")
    plt.plot(mean, label = "mean")
    plt.plot(mean, label = "meanAdded")
    plt.plot(mean, label = "meanSubtracted")
    plt.legend()
    plt.savefig("figure2.png")
    plt.clf()


### plot_3():
    median = np.median(zeros, axis = 0)
    added = median + std 
    subtracted = median - std  
    df = pd.DataFrame(median)
    df1 = pd.DataFrame(added)
    df2 = pd.DataFrame(subtracted)

    #df.plot()
    axis = [0,300,-256,100]
    plt.axis(axis)
    plt.title("Figure3 - median of 1000 trials with unlimited bankroll")
    plt.xlabel("Trials")
    plt.ylabel("winnings")
    plt.plot(median, label = "median")
    plt.plot(added, label = "medianAdded")
    plt.plot(subtracted, label = "medianSubtracted")
    plt.legend()
    plt.savefig("figure3.png")
    plt.clf()

def ex_plot_2(res):
    ##plot_4():
    index = 1000
    zeros = np.full((1000,1001), 0)
    for i in range(index):
        cur = simulator_exp2(.60)

        zeros[i] = cur
    mean  = np.mean(zeros, axis = 0)
    std = np.std(zeros, axis = 0)
    added = mean + std
    subtracted = mean - std
    
    
    np.mean(zeros) 
    df = pd.DataFrame(mean)
    df1 = pd.DataFrame(added)
    df2 = pd.DataFrame(subtracted)

    #df.plot()
    axis = [0,300,-256,100]
    plt.axis(axis)
    plt.title("Figure4 - mean of 1000 trials with limited bankroll")
    plt.xlabel("Trials")
    plt.ylabel("winnings")
    plt.plot(mean, label = "mean")
    plt.plot(mean, label = "meanAdded")
    plt.plot(mean, label = "meanSubtracted")
    plt.legend()
    plt.savefig("figure4.png")
    plt.clf()

    ##plot_5():
    median = np.median(zeros, axis = 0)
    added = median + std 
    subtracted = median - std  
    df = pd.DataFrame(median)
    df1 = pd.DataFrame(added)
    df2 = pd.DataFrame(subtracted)

    #df.plot()
    axis = [0,300,-256,100]
    plt.axis(axis)
    plt.title("Figure5 - median of 1000 trials with limited bankroll")
    plt.xlabel("Trials")
    plt.ylabel("winnings")
    plt.plot(median, label = "median")
    plt.plot(added, label = "medianAdded")
    plt.plot(subtracted, label = "medianSubtracted")
    plt.legend()
    plt.savefig("figure5.png")
    plt.clf()



def simulator_exp1(win_prob):   
    res = np.zeros(1001)
    winnings = 0
    count = 0
    while winnings < 80:
        won = False
        bet_amount = 1
        while not won:
            if count >= 1001:
                return res
            res[count] = winnings
            won = get_spin_result(win_prob) 
            if won == False:
                winnings = winnings - bet_amount
                bet_amount = bet_amount * 2
            else:
                winnings = winnings + bet_amount
            count +=1
        plot_exp_1(res)
        #plot_2(res)
        #plot_3(res)
    return res 

def simulator_exp2(win_prob):   
    res = np.zeros(1001)
    winnings = 0
    count = 0
    bankroll = 256
    while winnings < 80:
        won = False
        bet_amount = 1
        while not won:
            if count >= 1001:
                return res
            res[count] = winnings
            won = get_spin_result(win_prob) 
            if won == False:
                winnings = winnings - bet_amount
                bet_amount = bet_amount * 2
                valueToCheck = winnings - bet_amount
                
                if winnings == -bankroll:
                    res[count:] = winnings
                    return res
                if valueToCheck < -bankroll:
                    bet_amount = bankroll + winnings
                    
            else:
                winnings = winnings + bet_amount
            count +=1
        #plot_2(res)
        #plot_3(res)
    return res 

  		  	   		  		 		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  		 		  		  		    	 		 		   		 		  
    test_code()  		  	   		  		 		  		  		    	 		 		   		 		  

