def solution():
    # Calculate the total cost of the sandwiches
    sandwiches_cost = 5 * 4  # 4 people buying sandwiches

    # Calculate the total cost of the fruit salads
    fruit_salad_cost = 3 * 4  # 4 people buying fruit salads

    # Calculate the total cost of the sodas
    sodas_cost = 2 * 2 * 4  # 2 sodas per person for 4 people

    # Calculate the total cost of the snack bags
    snack_bags_cost = 4 * 3  # 3 bags of snacks for 4 people

    # Calculate the total cost of the picnic basket contents
    total_cost = sandwiches_cost + fruit_salad_cost + sodas_cost + snack_bags_cost
    result = total_cost
    return result

print(solution())