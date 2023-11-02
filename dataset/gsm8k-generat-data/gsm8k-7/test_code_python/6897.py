def solution():
    weekly_pay = 100
    arcade_spending = weekly_pay / 2
    food_spending = 10

    # Calculate the amount spent on arcade tokens
    token_spending = arcade_spending - food_spending

    # Calculate the number of hours Mike can play with the tokens
    hours_played = token_spending / 8

    # Convert the hours to minutes
    minutes_played = hours_played * 60
    result = minutes_played
    return result

print(solution())