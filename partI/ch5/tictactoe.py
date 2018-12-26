theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printboard(board):

	for i in board:
		print(board[i]+" ",end="")

		if 'R' in i :
			print(" ")
		else : 
			print("| ",end="")


turn = 'X'

for i in range(9):

	print("Print where you want to place a {}".format(turn))

	loc = input()	
	if theBoard[loc] is not " ":
		print("The place is already occupied . Please enter another ! ")
		continue

	theBoard[loc] = turn

	if turn is 'X' : 
		turn = 'O'

	else:
		turn = 'X'

	print("\nThe tic-tac-toe board looks like : ")	
	printboard(theBoard)
	print("")










