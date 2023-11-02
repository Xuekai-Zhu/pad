def solution():
    # Define the number of people attending the picnic
    num_people = 4

    # Calculate the total cost of the sandwiches
    sandwich_cost = 5 * num_people

    # Calculate the total cost of the fruit salads
    fruit_salad_cost = 3 * num_people

    # Calculate the total cost of the sodas
    soda_cost = 2 * 2 * num_people

    # Calculate the total cost of the snack bags
    snack_cost = 3 * 4

    # Calculate the total cost of the picnic basket
    total_cost = sandwich_cost + fruit_salad_cost + soda_cost + snack_cost
    result = total_cost
    return result

print(solution())