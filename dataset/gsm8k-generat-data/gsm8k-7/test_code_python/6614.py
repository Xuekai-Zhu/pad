def solution():
    num_snakes = 3
    num_eggs_per_snake = 2
    num_total_eggs = num_snakes * num_eggs_per_snake
    regular_price = 250
    rare_price = 4 * regular_price
    
    # Calculate the total revenue from selling regular snakes
    regular_revenue = (num_total_eggs - 1) * regular_price
    
    # Calculate the revenue from selling the super rare snake
    rare_revenue = rare_price
    
    # Calculate the total revenue from selling all the snakes
    total_revenue = regular_revenue + rare_revenue
    result = total_revenue
    return result

print(solution())