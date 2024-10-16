from lab04 import solveMaze


def test_solveMaze1():
    maze1 = [
['+','+','+','+',' ','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ','G','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
    assert solveMaze(maze1,4,4) == True
    assert maze1 == [['+', '+', '+', '+', ' ', '+'],
                     ['+', 8, '+', ' ', ' ', '+'],
                     ['+', 7, 9, 'G', '+', '+'],
                     ['+', 6, '+', '+', 2, '+'],
                     ['+', 5, 4, 3, 1, '+'],
                     ['+', '+', '+', '+', '+', '+']]
    maze1 = [
['+','+','+','+',' ','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ','G','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]

    assert solveMaze(maze1,2,2) == True
    assert maze1 == [['+', '+', '+', '+', ' ', '+'],
                     ['+', 3, '+', ' ', ' ', '+'],
                     ['+', 2, 1, 'G', '+', '+'],
                     ['+', 4, '+', '+', 9, '+'],
                     ['+', 5, 6, 7, 8, '+'],
                     ['+', '+', '+', '+', '+', '+']]
    

def test_solveMaze2():
    maze2 = [
['+','+','+','+','+','+'],
['+',' ','+',' ','G','+'],
['+',' ',' ',' ','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
    assert solveMaze(maze2,1,1) == True
    assert maze2 == [['+', '+', '+', '+', '+', '+'],
                     ['+', 1, '+', 11, 'G', '+'],
                     ['+', 2, 9, 10, '+', '+'],
                     ['+', 3, '+', '+', 8, '+'],
                     ['+', 4, 5, 6, 7, '+'],
                     ['+', '+', '+', '+', '+', '+']]

def test_solveMaze3():
    maze3 = [
['+','+','+','+','+','+'],
['+',' ',' ',' ','+','+'],
['+',' ',' ',' ','+','+'],
['+',' ',' ','+','+','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
    assert solveMaze(maze3,4,2) == False
    assert maze3 == [['+', '+', '+', '+', '+', '+'],
                     ['+', 5, 4, 9, '+', '+'],
                     ['+', 6, 3, 10, '+', '+'],
                     ['+', 7, 2, '+', '+', '+'],
                     ['+', 8, 1, 11, 12, '+'],
                     ['+', '+', '+', '+', '+', '+']]

def test_solveMaze4():
    maze4 = [
['+','+','+','+','+','+'],
['+',' ',' ',' ','G','+'],
['+','+',' ',' ',' ','+'],
['+',' ','+','+','+','+'],
['+','+',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]
    assert solveMaze(maze4,3,1) == False
    assert maze4 == [['+', '+', '+', '+', '+', '+'],
                     ['+', ' ', ' ', ' ', 'G', '+'],
                     ['+', '+', ' ', ' ', ' ', '+'],
                     ['+', 1, '+', '+', '+', '+'],
                     ['+', '+', ' ', ' ', ' ', '+'],
                     ['+', '+', '+', '+', '+', '+']]

def test_solveMaze5():
    maze5 = [[' ']]
    assert solveMaze(maze5,0,0) == False
    assert maze5 == [[1]]



    

    
    

    

   
    
                     


    
