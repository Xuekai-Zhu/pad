def solution():
    """Jake has 3 snakes. Each of them lays 2 eggs. Most of the baby snakes sell for $250 but one super rare one costs 4 times as much. How much did he get from selling the snakes?"""
    # Define the number of snakes and eggs
    snakes = 3
    eggs_per_snake = 2

    # Calculate the number of baby snakes
    baby_snakes = snakes * eggs_per_snake

    # Calculate the earnings from selling most of the baby snakes
    normal_snakes_earnings = (baby_snakes - 1) * 250

    # Calculate the earnings from selling the super rare snake
    rare_snake_earnings = 4 * 250

    # Calculate the total earnings
    total_earnings = normal_snakes_earnings + rare_snake_earnings

    result = total_earnings
    return result

print(solution())