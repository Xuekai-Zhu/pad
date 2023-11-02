def solution():
    num_chickens = 20
    eggs_per_chicken = 6
    eggs_per_carton = 12

    # Calculate the total number of eggs on the farm
    total_eggs = num_chickens * eggs_per_chicken

    # Calculate the total number of egg cartons that can be filled
    num_cartons = total_eggs // eggs_per_carton
    result = num_cartons
    return result

print(solution())