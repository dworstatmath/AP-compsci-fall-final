grid = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
players = ["X","O"]
wins=[]
moves=[[],[]]
def row(num,m):
    message=""
    for i in range(m):
        message+="|"+grid[num*m+i]
    return message
def draw_grid(m):
    for i in range (m):
        print("\033[4m"+row(i,m))
def find_winning_moves (m):
    for i in range(m):
        row=[]
        for j in range(m):
            row.append(m*i+j)
        wins.append(row)
    for i in range(m):
        row=[]
        for j in range(m):
            row.append(i+m*j)
        wins.append(row)
    for i in range(m):
        row=[]
        for j in range(m):
            row.append((m*i+j*(m+1))%m**2)
        wins.append(row)
    for i in range(m):
        row=[]
        for j in range(m):
            row.append((m*i+j*(m-1)+m-1)%m**2)
        wins.append(row)
def game(m):
    x=0
    draw_grid(m)
    find_winning_moves (m)
    for move in range(m**2):
        place=grid.index(input("Where does "+ players[move%2]+" want to go?"))
        grid[place]=players[move%2]
        draw_grid(m)
        moves[move%2].append(place)
        for win in wins:
            if set(win).issubset(moves[move%2]):
                x=1
                print(players[move%2]+" wins!")
                break
        if(x==1):
            break
game(4)