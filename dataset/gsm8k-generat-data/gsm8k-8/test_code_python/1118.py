def solution():
    # Define the variables for each person's number of wins
    dana_wins = x
    perry_wins = x + 5
    charlie_wins = x - 2
    phil_wins = charlie_wins + 3

    # Set up an equation to solve for x (number of wins by Dana)
    # The sum of all wins equals 12 (Phil's wins)
    # x + (x+5) + (x-2) + (x-2+3) = 12
    # Simplify and solve for x
    x = 2
    
    # Calculate Perry's number of wins
    perry_wins = x + 5

    # Calculate the difference in wins between Perry and Phil
    difference = perry_wins - phil_wins
    result = difference
    return result

print(solution())