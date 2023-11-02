def solution():
    num_pizzas = 6
    slices_per_pizza = 12
    num_games = 8

    # Calculate the total number of slices of pizza needed
    total_slices = num_pizzas * slices_per_pizza

    # Calculate the total number of goals scored
    total_goals = total_slices

    # Calculate the average number of goals per game
    avg_goals_per_game = total_goals / num_games
    result = avg_goals_per_game
    return result

print(solution())