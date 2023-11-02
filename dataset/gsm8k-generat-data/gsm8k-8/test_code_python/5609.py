def solution():
    # Define the total playtime in hours
    total_playtime = 4 * 7 * 2

    # Calculate the percentage of the game completed
    percentage_completed = 40/100

    # Calculate how much of the game is left
    game_left = 1 - percentage_completed

    # Calculate the remaining playtime needed to finish the game
    remaining_playtime = game_left * total_playtime

    # Calculate how many days it will take to finish the game
    days_to_finish = remaining_playtime / (7 - 4)

    result = days_to_finish
    return result

print(solution())