# 8-queens solver with genetic algorithm implementation
# unit tests

import unittest
from player import creature, population

class GATests(unittest.TestCase):

    def test_fitness_function(self):
        
        # test boards
        S = []
        S.append([0,0,0,0,0,0,0,0])
        S.append([2,1,4,3,7,5,6,0]) 
        S.append([6,5,2,0,4,1,3,5]) 
        S.append([2,4,7,5,3,6,7,0]) 
        S.append([3,5,6,1,1,3,4,2]) 
        S.append([2,4,6,0,3,1,7,5]) 
        truth = [0, 19, 22, 24, 21, 28]
    
        for i in range(len(S)):
            thing = creature(8, S[i])
            val = thing.fitness()
            self.assertEqual(val, truth[i], msg=("Incorrect Fitness Computed"))
    
    def test_survival_distro(self):
    
        # test boards
        S = []
        S.append([0,0,0,0,0,0,0,0])
        S.append([2,1,4,3,7,5,6,0]) 
        S.append([6,5,2,0,4,1,3,5]) 
        S.append([2,4,7,5,3,6,7,0]) 
        S.append([3,5,6,1,1,3,4,2]) 
        S.append([2,4,6,0,3,1,7,5]) 
        truth = [19, 22, 24, 21, 28]
        order = [5, 3, 2, 4, 1, 0]    
    
        pop = population(6, 8, 0.001, S)
        pop.rank_fitness()
        survival_distro = pop.choose_survivors()
        for i in range(4):
            diff_check = survival_distro[order[i]] > survival_distro[order[i+1]]
            self.assertTrue(diff_check, msg=("Distro is incorrect!"))
    
    def test_breeding(self):
        pass


if __name__ == '__main__':
    unittest.main()

