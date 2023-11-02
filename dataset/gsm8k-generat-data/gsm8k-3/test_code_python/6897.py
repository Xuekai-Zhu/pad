def solution():
    """Mike gets paid 100 dollars a week.  He decides to spend half of that at an arcade.  He spends 10 dollars at the arcade on food and uses the rest on arcade tokens. He can play for 1 hour for $8. How many minutes can he play?"""
    # Define Mike's weekly pay and the amount he spends at the arcade
    weekly_pay = 100
    arcade_spending = weekly_pay / 2 + 10

    # Determine how much Mike can spend on arcade tokens
    token_spending = arcade_spending - 10

    # Calculate how many hours Mike can play with his token spending
    hours_played = token_spending / 8

    # Calculate how many minutes Mike can play
    minutes_played = hours_played * 60

    # Display how many minutes Mike can play
    result = minutes_played
    return result

print(solution())