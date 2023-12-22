#!/usr/bin/env python3
from FourConnect import * # See the FourConnect.py file
import csv
import copy
import time
def move_order_heuristic():
    # Define the center column as the most preferred and score other columns based on their distance from the center
    center_column = 3
    column_order = [center_column] + [i for i in range(7) if i != center_column]
    # Sort the columns based on their distance from the center, with the center being the most preferred
    column_order.sort(key=lambda col: abs(col - center_column))
    return column_order
####################################################################################################################
class GameTreePlayer:
    def __init__(self):
        self.depth = 5  # You can change the depth as needed
        self.player = 2  # This player
        self.count = 0
        pass
    
    def FindBestAction(self,currentState):
        game = FourConnect()
        game.SetCurrentState(currentState)
        alpha = float('-inf')
        beta = float('inf')
        # use line 27 when using alpha beta pruning or move order heuristics
        _, action = self.minimax(game, self.depth, alpha, beta, True)
        # use line 28 when not using alpha beta pruning simple minimax
        # _, action = self.minimax(game, self.depth, True)
        return action
    
########################################################################################################
# Minimax without alpha beta pruning
    # def minimax(self, game, depth, is_maximizing_player):
    #     # Base case: check if game is over or depth is reached
    #     self.count += 1
    #     if depth == 0 or game.winner is not None:
    #         return self.evaluate1(game), None #change evaluate function 
        
    #     if is_maximizing_player:  # Maximizing for player 2
    #         best_score = float('-inf')
    #         best_action = None
    #         for action in range(7):  # There are 7 columns in FourConnect
    #             if game._CoinRowAfterAction(action) != -1:  # Check if action is legal
    #                 # Try the action
    #                 game_copy = copy.deepcopy(game)
    #                 game_copy.GameTreePlayerAction(action)
    #                 score, _ = self.minimax(game_copy, depth - 1, False)
    #                 # Choose the best scoring action
    #                 if score > best_score:
    #                     best_score = score
    #                     best_action = action
    #         return best_score, best_action
    #     else:  # Minimizing for player 1
    #         best_score = float('inf')
    #         best_action = None
    #         for action in range(7):
    #             if game._CoinRowAfterAction(action) != -1:  # Check if action is legal
    #                 # Try the action
    #                 game_copy = copy.deepcopy(game)
    #                 game_copy.MyopicPlayerAction()  # Assume myopic player makes a random valid action
    #                 score, _ = self.minimax(game_copy, depth - 1, True)
    #                 # Choose the action that leads to the worst scenario for player 2
    #                 if score < best_score:
    #                     best_score = score
    #                     best_action = action
    #         return best_score, best_action
###############################################################################################################
# Minimax with alpha beta pruning
    # def minimax(self, game, depth, alpha, beta, is_maximizing_player):
    #     # Base case: check if game is over or depth is reached
    #     self.count += 1
    #     if depth == 0 or game.winner is not None:
    #         return self.evaluate3(game), None #change evaluate function 

    #     if is_maximizing_player:  # Maximizing for player 2
    #         best_score = float('-inf')
    #         best_action = None
    #         for action in range(7):  # There are 7 columns in FourConnect
    #             if game._47_CoinRowAfterAction(action) != -1:  # Check if action is legal
    #                 # Try the action
    #                 game_copy = copy.deepcopy(game)
    #                 game_copy.GameTreePlayerAction(action)
    #                 score, _ = self.minimax(game_copy, depth - 1, alpha, beta, False)
    #                 # Choose the best scoring action
    #                 if score > best_score:
    #                     best_score = score
    #                     best_action = action
    #                 alpha = max(alpha, best_score)
    #                 if beta <= alpha:
    #                     break  # beta cut-off
    #         return best_score, best_action
    #     else:  # Minimizing for player 1
    #         best_score = float('inf')
    #         best_action = None
    #         for action in range(7):
    #             if game._47_CoinRowAfterAction(action) != -1:  # Check if action is legal
    #                 # Try the action
    #                 game_copy = copy.deepcopy(game)
    #                 game_copy.MyopicPlayerAction()  # Assume myopic player makes a random valid action
    #                 score, _ = self.minimax(game_copy, depth - 1, alpha, beta, True)
    #                 # Choose the action that leads to the worst scenario for player 2
    #                 if score < best_score:
    #                     best_score = score
    #                     best_action = action
    #                 beta = min(beta, best_score)
    #                 if beta <= alpha:
    #                     break  # alpha cut-off
    #         return best_score, best_action
##############################################################################################################
# Minimax with alpha beta pruning with moving order heuristics
    def minimax(self, game, depth, alpha, beta, is_maximizing_player):
        # Base case: check if game is over or depth is reached
        self.count += 1
        if depth == 0 or game.winner is not None:
            return self.evaluate2(game), None #change evaluate function 

        if is_maximizing_player:  # Maximizing for player 2
            best_score = float('-inf')
            best_action = None
            for action in move_order_heuristic():  # There are 7 columns in FourConnect
                if game._47_CoinRowAfterAction(action) != -1:  # Check if action is legal
                    # Try the action
                    game_copy = copy.deepcopy(game)
                    game_copy.GameTreePlayerAction(action)
                    score, _ = self.minimax(game_copy, depth - 1, alpha, beta, False)
                    # Choose the best scoring action
                    if score > best_score:
                        best_score = score
                        best_action = action
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break  # beta cut-off
            return best_score, best_action
        else:  # Minimizing for player 1
            best_score = float('inf')
            best_action = None
            for action in move_order_heuristic():
                if game._47_CoinRowAfterAction(action) != -1:  # Check if action is legal
                    # Try the action
                    game_copy = copy.deepcopy(game)
                    game_copy.MyopicPlayerAction()  # Assume myopic player makes a random valid action
                    score, _ = self.minimax(game_copy, depth - 1, alpha, beta, True)
                    # Choose the action that leads to the worst scenario for player 2
                    if score < best_score:
                        best_score = score
                        best_action = action
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break  # alpha cut-off
            return best_score, best_action

###########################################################################################################
# evaluation function 1
    def evaluate1(self, game):
        # For simplicity, let's assume that a win is worth +1, loss is worth -1, and draw is 0
        if game.winner == self.player:
            return 1  # Win
        elif game.winner is not None:
            return -100  # Loss
        else:
            return 0  # Draw or game continuing
   
###########################################################################################################
# evaluation function 2

    def count_consecutives(self,board, player):
        # Initialize counts
        fours = threes = twos = 0
        
        # Check rows for consecutive twos, threes, and fours
        for row in board:
            for col in range(0, len(row) - 3):  # Only need to check starting up to the 4th last column
                window = row[col:col + 4]
                fours += window.count(player) == 4
                if window.count(player) == 3 and window.count(0) == 1:
                    threes += 1
                if window.count(player) == 2 and window.count(0) == 2:
                    twos += 1

        # Check columns for consecutive twos, threes, and fours
        for col in range(0, len(board[0])):
            column = [row[col] for row in board]
            for row in range(0, len(column) - 3):  # Only need to check starting up to the 4th last row
                window = column[row:row + 4]
                fours += window.count(player) == 4
                if window.count(player) == 3 and window.count(0) == 1:
                    threes += 1
                if window.count(player) == 2 and window.count(0) == 2:
                    twos += 1

        # Check for diagonals for consecutive twos, threes, and fours
        for row in range(0, len(board) - 3):
            for col in range(0, len(board[0]) - 3):
                # Check for downward diagonals (top-left to bottom-right)
                window = [board[row + i][col + i] for i in range(4)]
                fours += window.count(player) == 4
                if window.count(player) == 3 and window.count(0) == 1:
                    threes += 1
                if window.count(player) == 2 and window.count(0) == 2:
                    twos += 1

                # Check for upward diagonals (bottom-left to top-right)
                if col + 3 < len(board[0]) and row - 3 >= 0:
                    window = [board[row - i][col + i] for i in range(4)]
                    fours += window.count(player) == 4
                    if window.count(player) == 3 and window.count(0) == 1:
                        threes += 1
                    if window.count(player) == 2 and window.count(0) == 2:
                        twos += 1

        return fours, threes, twos

    def evaluate2(self, game):
        curr_state = game.GetCurrentState()
        player = self.player
        opponent = 1 if player == 2 else 2
        my_fours, my_threes, my_twos = self.count_consecutives(curr_state, player)
        comp_fours, comp_threes, comp_twos = self.count_consecutives(curr_state, opponent)

        utility_value = (my_fours * 1000 + my_threes * 5 + my_twos * 2) - (comp_fours * 1000 + comp_threes * 5 + comp_twos * 2)
        return utility_value

###########################################################################################################
# evaluation function 3
    def evaluate3(self, game):
        score = 0
        board = game.GetCurrentState()
        player = self.player
        # Define a list of directions: right, down, down-right, and up-right
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]

        # Function to count consecutive pieces in a direction
        def count_consecutive(board, player, direction, start_x, start_y):
            count = 0
            x, y = start_x, start_y
            for _ in range(4): # Look for four in a row
                if 0 <= x < 7 and 0 <= y < 6 and board[y][x] == player:
                    count += 1
                    x += direction[0]
                    y += direction[1]
                else:
                    break
            return count

        # Count potential winning lines for the current player
        for y in range(6):
            for x in range(7):
                for direction in directions:
                    if count_consecutive(board, player, direction, x, y) == 4:
                        score += 100 # Assign a score for a winning position

        # Count potential winning lines for the opponent and subtract their score
        opponent = 1 if player == 2 else 2
        for y in range(6):
            for x in range(7):
                for direction in directions:
                    if count_consecutive(board, opponent, direction, x, y) == 4:
                        score -= 100 # Subtract a score if the opponent has a winning position

        return score
##########################################################################################################################
# evaluation function 4
# weighted average of all above three evaluation function
    def evaluate4(self,game):
        weight1 = 0.1
        weight2 = 0.4
        weight3 = 0.5
        score = self.evaluate1(game)*weight1 + self.evaluate2(game)*weight2 + self.evaluate3(game)*weight3
        return score

##########################################################################################################################    
def LoadTestcaseStateFromCSVfile():
    testcaseState=list()
    with open('testcase_easy1.csv', 'r') as read_obj: 
       	csvReader = csv.reader(read_obj)
        for csvRow in csvReader:
            row = [int(r) for r in csvRow]
            testcaseState.append(row)
        return testcaseState


def PlayGame():
    wins = 0
    total_moves = 0
    win_time = 0
    recursive_calls = 0
    num_games = 50  # Set the number of games you want to play

    for _ in range(num_games):
        start_time = time.time()  # Start timing
        fourConnect = FourConnect()
        gameTree = GameTreePlayer()
        
        move = 0
        while move < 42:  # At most 42 moves are possible
            if move % 2 == 0:  # Myopic player always moves first
                fourConnect.MyopicPlayerAction()
            else:
                currentState = fourConnect.GetCurrentState()
                gameTreeAction = gameTree.FindBestAction(currentState)
                if gameTreeAction is not None:  # Only play if a valid move was found
                    fourConnect.GameTreePlayerAction(gameTreeAction)
            move += 1
            if fourConnect.winner == 2:
                wins += 1
                total_moves += move
                win_time += time.time()-start_time
                break
            elif fourConnect.winner is not None:  # If the other player wins
                break
            
        recursive_calls += gameTree.count
        # Check for a drawn game
        if fourConnect.winner == None:
            print("Game is drawn.")
        else:
            print("Winner: Player {}\n".format(fourConnect.winner))

        print("Moves: {}".format(move))

    # Calculate average moves per win and total execution time
    average_moves = total_moves / wins if wins > 0 else float('inf')
    if(wins != 0):
        execution_time = win_time/wins  # End timing
    else:
        execution_time = 0

    # Print results
    print(f"Results: {wins} wins out of {num_games} games, {average_moves} average moves per win")
    print(f"Total win time for {num_games} game(s): {execution_time:.2f} seconds")
    print(f"Total recursion calls for {num_games} game(s): {recursive_calls}")

def RunTestCase():
    """
    This procedure reads the state in testcase.csv file and start the game.
    Player 2 moves first. Player 2 must win in 5 moves to pass the testcase; Otherwise, the program fails to pass the testcase.
    """
    
    fourConnect = FourConnect()
    gameTree = GameTreePlayer()
    testcaseState = LoadTestcaseStateFromCSVfile()
    fourConnect.SetCurrentState(testcaseState)
    fourConnect.PrintGameState()

    move=0
    while move<5: #Player 2 must win in 5 moves
        if move%2 == 1: 
            fourConnect.MyopicPlayerAction()
        else:
            currentState = fourConnect.GetCurrentState()
            gameTreeAction = gameTree.FindBestAction(currentState)
            fourConnect.GameTreePlayerAction(gameTreeAction)
        fourConnect.PrintGameState()
        move += 1
        if fourConnect.winner!=None:
            break
    
    print("Roll no : 2020B3A71159G") #Put your roll number here
    
    if fourConnect.winner==2:
        print("Player 2 has won. Testcase passed.")
    else:
        print("Player 2 could not win in 5 moves. Testcase failed.")
    print("Moves : {0}".format(move))
    

def main():
    
    #PlayGame()

    """
    You can modify PlayGame function for writing the report
    Modify the FindBestAction in GameTreePlayer class to implement Game tree search.
    You can add functions to GameTreePlayer class as required.
    """

    """
        The above code (PlayGame()) must be COMMENTED while submitting this program.
        The below code (RunTestCase()) must be UNCOMMENTED while submitting this program.
        Output should be your rollnumber and the bestAction.
        See the code for RunTestCase() to understand what is expected.
    """
    
    RunTestCase()


if __name__=='__main__':
    main()