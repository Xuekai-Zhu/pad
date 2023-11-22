def solution():
    
    # Define the initial number of games
    games = 5

    # Calculate the total amount of money Steve saves each year
    savings_year1 = 12 * 1 * games
    savings_year2 = 12 * 2 * games
    savings_year3 = 4 * games
    total_savings = savings_year1 + savings_year2 + savings_year3

    # Calculate the total number of games Steve gets for Christmas
    christmas_games = 5

    # Calculate the total number of games Steve has after 3 years
    total_games = total_savings + christmas_games

    # Display the total number of games Steve has after 3 years
    result = total_games
    return result

print(solution())