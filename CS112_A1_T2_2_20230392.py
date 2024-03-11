# Check if the number has not been chosen already
def validity(my_list, step, numbers):
    if step in numbers:
        numbers.remove(step)
        my_list.append(step)
        return True
    else:
        return False


# Set up the game
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = []
list2 = []
print("Game of: Number scrabble")
player1 = input(f'Player 1, please enter your name: ')
player2 = input('Player 2, please enter your name: ')
current_player = 1

while True:
    print(f"It is your turn: {player1 if current_player == 1 else player2}")
    print(f'Please choose a number from this list: {numbers}')

    try:
        step = int(input("Please pick a number from 1 to 9: "))
        if 1 <= step <= 9:
            # The first player's turn
            if current_player == 1:
                player_name = player1
                if validity(list1, step, numbers):
                    print(f"{player1}'s selected numbers: {list1}")
                    for x in list1:
                        for y in list1:
                            for z in list1:
                                if x != y and y != z and x != z and x + y + z == 15:
                                    print(f"{player1}, you are a winner")
                                    exit()
                    current_player = 3 - current_player
                else:
                    print("The number has already been selected. Please enter another number.")
            # The second player's turn
            else:
                player_name = player2
                if validity(list2, step, numbers):
                    print(f"{player2}'s selected numbers: {list2}")
                    for a in list2:
                        for b in list2:
                            for c in list2:
                                if a != b and b != c and a != c and a + b + c == 15:
                                    print(f"{player2}, you are a winner")
                                    exit()
                    current_player = 3 - current_player
                else:
                    print("The number has already been selected. Please enter another number.")
        else:
            print("Please enter a number from 1 to 9")
    except ValueError:
        print("Please enter a valid number")
        continue

    # If the list is empty (all numbers have been selected)
    if not numbers:
        print("The game is a draw.")
        break
