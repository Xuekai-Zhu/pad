def solution():
    # Calculate the total number of eggs laid by the snakes
    total_eggs = 3 * 2

    # Calculate the total revenue from selling most of the baby snakes
    regular_snake_revenue = (total_eggs - 1) * 250  # All but the rare snake sell for $250 each

    # Calculate the revenue from selling the rare snake
    rare_snake_revenue = 4 * 250  # The rare snake sells for 4 times the price of a regular snake

    # Calculate the total revenue from selling all the snakes
    total_revenue = regular_snake_revenue + rare_snake_revenue
    result = total_revenue
    return result

print(solution())