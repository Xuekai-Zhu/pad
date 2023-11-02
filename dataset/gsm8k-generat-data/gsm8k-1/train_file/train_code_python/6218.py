def solution():
    """Theo and Tia are buying food for their picnic basket. They invited two of their friends. They buy individual sandwiches and individual fruit salads. They buy two sodas per person and 3 bags of snacks to share for their friends and themselves. Sandwiches are $5 each. Fruit salad is $3 each. Sodas are $2 each. The snack bags are $4 each. How much did they spend on the entire contents of their picnic basket?"""
    num_people = 4
    sandwiches_per_person = 1
    fruit_salads_per_person = 1
    sodas_per_person = 2
    num_snack_bags = 3
    sandwich_cost = 5
    fruit_salad_cost = 3
    soda_cost = 2
    snack_bag_cost = 4
    
    total_sandwiches = num_people * sandwiches_per_person
    total_fruit_salads = num_people * fruit_salads_per_person
    total_sodas = num_people * sodas_per_person
    total_snack_bags = num_snack_bags
    total_cost = (total_sandwiches * sandwich_cost) + (total_fruit_salads * fruit_salad_cost) + (total_sodas * soda_cost) + (total_snack_bags * snack_bag_cost)
    
    result = total_cost
    return result

print(solution())