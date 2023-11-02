def solution():
    """Theo and Tia are buying food for their picnic basket. They invited two of their friends. They buy individual sandwiches and individual fruit salads. They buy two sodas per person and 3 bags of snacks to share for their friends and themselves. Sandwiches are $5 each. Fruit salad is $3 each. Sodas are $2 each. The snack bags are $4 each. How much did they spend on the entire contents of their picnic basket?"""
    num_people = 4
    sandwiches_cost = 5
    fruit_salad_cost = 3
    sodas_cost = 2
    snacks_cost = 4
    sandwiches_count = num_people
    fruit_salad_count = num_people
    sodas_count = num_people * 2
    snacks_count = 3
    total_cost = (sandwiches_count * sandwiches_cost) + (fruit_salad_count * fruit_salad_cost) + (sodas_count * sodas_cost) + (snacks_count * snacks_cost)
    result = total_cost
    return result

print(solution())