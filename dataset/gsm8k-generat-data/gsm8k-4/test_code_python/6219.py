def solution():
    """Theo and Tia are buying food for their picnic basket. They invited two of their friends. They buy individual sandwiches and individual fruit salads. They buy two sodas per person and 3 bags of snacks to share for their friends and themselves. Sandwiches are $5 each. Fruit salad is $3 each. Sodas are $2 each. The snack bags are $4 each. How much did they spend on the entire contents of their picnic basket?"""
    # Define the number of people at the picnic
    num_people = 4

    # Calculate the cost of sandwiches and fruit salads for each person
    sandwich_cost = 5
    fruit_salad_cost = 3

    # Calculate the cost of sodas for each person
    sodas_cost = 2 * 2  # 2 sodas per person

    # Calculate the cost of snack bags to share
    snack_cost = 4 * 3  # 3 bags of snacks to share

    # Calculate the total cost for all items
    total_cost = (sandwich_cost + fruit_salad_cost + sodas_cost) * num_people + snack_cost

    # return the result
    result = total_cost
    return result

print(solution())