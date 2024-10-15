from Stack import Stack

def printMaze(maze):
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            print("|{:<2}".format(maze[row][col]), sep='',end='')
        print("|")
    return


def solveMaze(maze, startX, startY):
    s = Stack()
    s.push((startX, startY))
    step = 1
    maze[startX][startY] = step
    d = [(-1,0),(0,-1),(1,0),(0,1)]
    while s.isEmpty() == False:
        x,y = s.pop()
        for dx,dy in d:
            nx,ny = x + dx, y + dy
            if 0 <= nx <len(maze) and 0 <= ny <len(maze[0]):
                if maze[nx][ny] == "G":
                    return True
                elif maze[nx][ny] == " ":
                    step +=1
                    maze[nx][ny] = step
                    s.push((x,y))
                    s.push((nx,ny))
                    break

    return False

