field = 0
def show_field():
    print('---------')
    print('| ' + field[0] + ' ' + field[1] + ' ' + field[2] + ' |')
    print('| ' + field[3] + ' ' + field[4] + ' ' + field[5] + ' |')
    print('| ' + field[6] + ' ' + field[7] + ' ' + field[8] + ' |')
    print('---------')


def get_num(player):
    num_x = 0
    for x in field:
        if x == player:
            num_x += 1
    return num_x


def check_field():
    for p in players:
        for row in range(3):
            if (field[row] == p  # rows
                    and field[row + 1] == p
                    and field[row + 2] == p):
                if p == "X":
                    x_win = True
                elif p == "O":
                    o_win = True
            elif (field[row] == p  # cols
                  and field[row + 3] == p
                  and field[row + 6] == p):
                if p == "X":
                    x_win = True
                elif p == "O":
                    o_win = True
        if (field[0] == p  # cols
                and field[4] == p
                and field[8] == p):
            if p == "X":
                x_win = True
            elif p == "O":
                o_win = True
        if (field[2] == p  # cols
                and field[4] == p
                and field[6] == p):
            if p == "X":
                x_win = True
            elif p == "O":
                o_win = True


def print_result():
    num_x = get_num("X")
    num_o = get_num("O")
    if num_x - num_o > 1 or num_o - num_x > 1 or (x_win and o_win):
        print('Impossible')
    elif not x_win and not o_win:
        if num_x + num_o > 8:
            print('Draw')
        else:
            print('Game not finished')
    elif x_win:
        print('X wins')
    elif o_win:
        print('O wins')


def analyze(col, row):
    global field
    if type(col) != int or type(row) != int:
        print("You should enter numbers!")
        return False
    if col > 3 or row > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    index = col + 5 - 3 * (row - 1)
    cell = field[index]
    if cell == "X" or cell == "O":
        print("This cell is occupied! Choose another one!")
        return False
    else:
        field = field[:index] + "X" + field[index + 1:]
        show_field()
        return True


field = input()
players = ["X", "O"]
x_win = False
o_win = False
show_field()
check_field()

print('Enter the coordinates:')
coords = input()
coords = coords.split(' ')
while True:
    if analyze(int(coords[0]), int(coords[1])):
        break
    coords = input()
    coords = coords.split(' ')