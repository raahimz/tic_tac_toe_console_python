grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
user_turn = 'x'
turn_index = 1
has_won = False


def output_grid():
    for row in grid:
        print(row)


def check_user_win():
    # Checking for horizontal
    for row in grid:
        if row[0] == row[1] and row[1] == row[2] and row[0] == row[2] and row[0] != 0:
            output_grid()
            print(f'{user_turn} won!')
            return True

    # Checking for vertical
    for i in range(0, 3):
        if grid[0][i] == grid[1][i] and grid[1][i] == grid[2][i] and grid[0][i] == grid[2][i] and grid[0][i] != 0:
            output_grid()
            print(f'{user_turn} won!')
            return True

    # Checking for diagnol
    if (grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2] and grid[0][0] == grid[2][2] and grid[0][0] != 0) or (grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0] and grid[0][2] == grid[2][0] and grid[2][0] != 0):
        output_grid()
        print(f'{user_turn} won!')
        return True

    return False


while not has_won:
    output_grid()

    if turn_index % 2 == 0:
        user_turn = 'y'
    else:
        user_turn = 'x'

    coord = input(f'[{user_turn}]: Enter the COORD (x,y) :: ').split(',')
    print(int(coord[1]))
    selected_coord = grid[int(coord[0])-1][int(coord[1])-1]
    if selected_coord == 0:
        grid[int(coord[0])-1][int(coord[1])-1] = user_turn
        has_won = check_user_win()
        turn_index += 1
    else:
        print('Spot already taken!... try again')
