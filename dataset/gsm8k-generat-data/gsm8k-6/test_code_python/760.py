def solution():
    # Calculate the total number of servings needed
    total_servings = 30 * 2

    # Calculate the total number of potatoes needed
    total_potatoes = 4 * total_servings

    # Calculate the total amount of salt needed in teaspoons
    total_salt_teaspoons = total_servings

    # Calculate the total number of salt containers needed
    total_salt_containers = (total_salt_teaspoons + 4) // 5   # Add 4 to round up if necessary

    # Calculate the total cost of potatoes
    total_potatoes_cost = total_potatoes * 0.10

    # Calculate the total cost of salt containers
    total_salt_containers_cost = total_salt_containers * 2

    # Calculate the total cost of food
    total_cost = total_potatoes_cost + total_salt_containers_cost

    result = total_cost
    return result

print(solution())