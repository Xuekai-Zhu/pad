def solution():
    """Tom bought his games for $200. They tripled in value and he then sold 40% of them. How much did he sell the games for?"""
    # Define the initial cost of the games and the percentage sold
    initial_cost = 200
    sold_percentage = 0.4

    # Calculate the new value of the games after tripling in value
    new_value = 3 * initial_cost

    # Calculate the number of games sold and their total value
    sold_value = sold_percentage * new_value

    # Display the value of the games sold
    result = sold_value
    return result

print(solution())