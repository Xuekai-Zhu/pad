def solution():
    # Calculate the amount of money Mike spends on arcade tokens
    arcade_spending = 100/2 - 10  # half of his weekly pay minus $10 for food
    # Calculate the number of hours Mike can play with the arcade tokens
    hours_played = arcade_spending / 8
    # Calculate the total number of minutes Mike can play
    minutes_played = hours_played * 60
    result = minutes_played
    return result

print(solution())