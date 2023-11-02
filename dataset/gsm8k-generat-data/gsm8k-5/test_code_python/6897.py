def solution():
    weekly_pay = 100  # Mike gets paid $100 per week
    arcade_spending = weekly_pay / 2  # Mike spends half of his pay at the arcade
    food_expenses = 10  # Mike spends $10 on food at the arcade

    # Calculate the amount of money Mike has left for arcade tokens
    arcade_tokens = arcade_spending - food_expenses

    # Calculate the number of hours Mike can play with the arcade tokens
    hours_played = arcade_tokens / 8

    # Convert the hours played to minutes played
    minutes_played = hours_played * 60
    result = minutes_played
    return result

print(solution())