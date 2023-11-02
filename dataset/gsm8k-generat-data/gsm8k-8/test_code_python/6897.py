def solution():
    # Calculate the amount Mike spends at the arcade
    arcade_spending = 50 + 10

    # Calculate the number of arcade tokens Mike can buy
    tokens = arcade_spending / 8

    # Calculate the number of minutes Mike can play
    minutes = tokens * 60

    result = minutes
    return result

print(solution())