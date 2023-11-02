def solution():
    """Theo and Tia are buying food for their picnic basket. They invited two of their friends. They buy individual sandwiches and individual fruit salads. They buy two sodas per person and 3 bags of snacks to share for their friends and themselves. Sandwiches are $5 each. Fruit salad is $3 each. Sodas are $2 each. The snack bags are $4 each. How much did they spend on the entire contents of their picnic basket?"""
    # Define the cost of each item
    SANDWICH_COST = 5
    FRUIT_SALAD_COST = 3
    SODA_COST = 2
    SNACK_BAG_COST = 4

    # Define the number of people attending the picnic
    num_people = 4

    # Calculate the cost of the sandwiches
    sandwich_cost = num_people * SANDWICH_COST

    # Calculate the cost of the fruit salads
    fruit_salad_cost = num_people * FRUIT_SALAD_COST

    # Calculate the cost of the sodas
    soda_cost = num_people * 2 * SODA_COST

    # Calculate the cost of the snack bags
    snack_bag_cost = 3 * SNACK_BAG_COST

    # Calculate the total cost
    total_cost = sandwich_cost + fruit_salad_cost + soda_cost + snack_bag_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())