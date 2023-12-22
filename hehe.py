#!/usr/bin/env python3
from FourConnect import * # See the FourConnect.py file
import csv


class GameTreePlayer:
    def __init__(self, player=2):
        self.player = player

    def FindBestAction(self, currentState):
        best_action, _ = self.alpha_beta(currentState, depth=5, alpha=float('-inf'), beta=float('inf'), maximizing_player=True)
        return best_action

    def alpha_beta(self, state, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.is_terminal_state(state):
            return None, self.evaluate_state(state)

        valid_actions = self.get_valid_actions(state)

        if maximizing_player:
            max_eval = float('-inf')
            best_action = None

            for action in valid_actions:
                new_state = self.perform_action(state, action)
                _, eval_value = self.alpha_beta(new_state, depth - 1, alpha, beta, False)

                if eval_value > max_eval:
                    max_eval = eval_value
                    best_action = action

                alpha = max(alpha, eval_value)
                if beta <= alpha:
                    break

            return best_action, max_eval

        else:  # Minimizing player
            min_eval = float('inf')
            best_action = None

            for action in valid_actions:
                new_state = self.perform_action(state, action)
                _, eval_value = self.alpha_beta(new_state, depth - 1, alpha, beta, True)

                if eval_value < min_eval:
                    min_eval = eval_value
                    best_action = action

                beta = min(beta, eval_value)
                if beta <= alpha:
                    break

            return best_action, min_eval

    def is_terminal_state(self, state):
        return FourConnect().winner is not None or all(row.count(0) == 0 for row in state)

    def evaluate_state(self, state):
        return self.evaluate1(FourConnect())

    def get_valid_actions(self, state):
        return [action for action in range(7) if state[0][action] == 0]

    def perform_action(self, state, action):
        new_state = [row.copy() for row in state]
        for row in range(5, -1, -1):
            if new_state[row][action] == 0:
                new_state[row][action] = self.player  # Assuming Player 2 is always the GameTreePlayer
                break
        return new_state

    def evaluate1(self, game):
        # For simplicity, let's assume that a win is worth +1, loss is worth -1, and draw is 0
        if game.winner == self.player:
            return 100  # Win
        elif game.winner is not None:
            return -100  # Loss
        else:
            return 0  # Draw or game continuing

def LoadTestcaseStateFromCSVfile():
    testcaseState=list()

    with open('testcase.csv', 'r') as read_obj: 
       	csvReader = csv.reader(read_obj)
        for csvRow in csvReader:
            row = [int(r) for r in csvRow]
            testcaseState.append(row)
        return testcaseState


def PlayGame(num_games=50):
    """
    This function plays the game multiple times and prints the number of times Player 2 wins against Player 1.
    """
    player2_wins = 0

    for game in range(num_games):
        fourConnect = FourConnect()
        gameTree = GameTreePlayer()

        move = 0
        while move < 42:  # At most 42 moves are possible
            if move % 2 == 0:
                fourConnect.MyopicPlayerAction()
            else:
                currentState = fourConnect.GetCurrentState()
                gameTreeAction = gameTree.FindBestAction(currentState)
                fourConnect.GameTreePlayerAction(gameTreeAction)
            move += 1
            # if fourConnect.winner is not None:
            #     break

        if fourConnect.winner == 2:
            player2_wins += 1

        print(f"Game {game + 1} - Winner: Player {fourConnect.winner}, Moves: {move}")

    print("\nTotal Player 2 wins:", player2_wins)
    print("Roll no : 2020B5A71157G")  # Put your roll number here

    print("Moves : {0}".format(move))

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
    
    print("Roll no : 2021H10309999") #Put your roll number here
    
    if fourConnect.winner==2:
        print("Player 2 has won. Testcase passed.")
    else:
        print("Player 2 could not win in 5 moves. Testcase failed.")
    print("Moves : {0}".format(move))
    

def main():
    
    PlayGame()
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
    
    # RunTestCase()


if __name__=='__main__':
    main()
