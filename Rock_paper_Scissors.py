#III. Rock/scissors/paper
def rps(p1, p2):
    r = 'rock'
    s = 'scissors'
    p = 'paper'
    if (p1 == p2):
        return 'Draw!'
    elif (p1 == r and p2 == s):
        return 'Player 1 won!'
    elif (p1 == p and p2 == r):
        return 'Player 1 won!'
    elif (p1 == s and p2 == p):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'