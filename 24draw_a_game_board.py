# Time for some fake graphics! Ask the user what size game board they want to draw, and draw it for them to the screen
# using Python’s print statement.


def hor():
    return " ---"

def one_mid():
    return "|"

def vert():
    return f" {0} |"

def create_top(x):
    return ''.join([hor()*x, "\n", one_mid(), vert()*x, "\n", hor()*x])

def create_bot(x):
    return ''.join(["\n", one_mid(), vert()*x, "\n", hor()*x])

def create_board(x, y):
        board = ''.join([create_top(x), (create_bot(x))*(y-1)])
        return board


columns = 3
rows = 3

b = create_board(columns, rows)


print(b)
