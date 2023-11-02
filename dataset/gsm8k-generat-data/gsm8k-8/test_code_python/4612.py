def solution():
    # Define the number of eggs and the cost per egg
    num_eggs = 30
    cost_per_egg = 5 / num_eggs

    # Define the selling price per egg
    selling_price = 0.2

    # Calculate the number of eggs needed to recover the cost
    num_eggs_needed = 5 / cost_per_egg

    # Calculate the number of eggs Samantha will have left after selling
    num_eggs_left = num_eggs - num_eggs_needed

    result = num_eggs_left
    return result

print(solution())