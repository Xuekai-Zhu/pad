def solution():
    """Tom bought his games for $200. They tripled in value and he then sold 40% of them. How much did he sell the games for?"""
    # Define the initial cost of the games
    initial_cost = 200

    # Triple the value of the games
    value = initial_cost * 3

    # Calculate the number of games sold (40% of total)
    games_sold = value * 0.4

    # Return the price the games were sold for
    result = games_sold
    return result

print(solution())