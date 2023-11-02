def solution():
    """Jake has 3 snakes.  Each of them lays 2 eggs.  Most of the baby snakes sell for $250 but one super rare one costs 4 times as much.  How much did he get from selling the snakes?"""
    # Define the number of snakes and eggs
    num_snakes = 3
    eggs_per_snake = 2

    # Calculate the total number of eggs
    total_eggs = num_snakes * eggs_per_snake

    # Calculate the total revenue from selling most of the baby snakes
    regular_snake_revenue = (total_eggs - 1) * 250

    # Calculate the revenue from selling the super rare snake
    super_rare_snake_revenue = 4 * 250

    # Calculate the total revenue from selling all the snakes
    total_revenue = regular_snake_revenue + super_rare_snake_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())