def solution():
    """Mike gets paid 100 dollars a week. He decides to spend half of that at an arcade. He spends 10 dollars at the arcade on food and uses the rest on arcade tokens. He can play for 1 hour for $8. How many minutes can he play?"""
    # Define the amount of money Mike spends at the arcade on tokens
    arcade_tokens = (100 / 2) - 10

    # Calculate the number of 1-hour blocks he can play
    hours_played = arcade_tokens // 8

    # Calculate the number of minutes he can play
    minutes_played = hours_played * 60

    # Return the result
    result = minutes_played
    return result

print(solution())