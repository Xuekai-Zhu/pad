def solution():
    num_people = 4
    num_sandwiches = num_people
    sandwich_price = 5

    num_fruit_salads = num_people
    fruit_salad_price = 3

    num_sodas = num_people * 2
    soda_price = 2

    num_snack_bags = 3
    snack_bag_price = 4

    # Calculate the total cost of all sandwiches
    total_sandwich_cost = num_sandwiches * sandwich_price

    # Calculate the total cost of all fruit salads
    total_fruit_salad_cost = num_fruit_salads * fruit_salad_price

    # Calculate the total cost of all sodas
    total_soda_cost = num_sodas * soda_price

    # Calculate the total cost of all snack bags
    total_snack_bag_cost = num_snack_bags * snack_bag_price

    # Calculate the total cost of the entire picnic basket
    total_cost = total_sandwich_cost + total_fruit_salad_cost + total_soda_cost + total_snack_bag_cost
    result = total_cost
    return result

print(solution())