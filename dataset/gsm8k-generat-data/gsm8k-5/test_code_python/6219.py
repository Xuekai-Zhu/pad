def solution():
    num_people = 4  # Theo and Tia invited two friends
    num_sandwiches = num_people  # They bought one sandwich per person
    num_fruit_salads = num_people  # They bought one fruit salad per person
    num_sodas = 2 * num_people  # They bought two sodas per person
    num_snack_bags = 3  # They bought three snack bags to share

    # Calculate the total cost of sandwiches
    cost_sandwiches = num_sandwiches * 5

    # Calculate the total cost of fruit salads
    cost_fruit_salads = num_fruit_salads * 3

    # Calculate the total cost of sodas
    cost_sodas = num_sodas * 2

    # Calculate the total cost of snack bags
    cost_snack_bags = num_snack_bags * 4

    # Calculate the total cost of the picnic basket
    total_cost = cost_sandwiches + cost_fruit_salads + cost_sodas + cost_snack_bags
    result = total_cost
    return result

print(solution())