def solution():
    """Five friends eat at Wendy's and ordered the following: a platter of Taco Salad that cost $10, 
    5 orders of Dave's Single hamburger that cost $5 each, 4 sets of french fries that cost $2.50, 
    and 5 cups of peach lemonade that cost $2 each. How much will each of them pay if they will split the bill equally?"""
    taco_salad_cost = 10
    hamburgers_cost = 5 * 5
    french_fries_cost = 4 * 2.5
    peach_lemonade_cost = 5 * 2
    total_cost = taco_salad_cost + hamburgers_cost + french_fries_cost + peach_lemonade_cost
    cost_per_person = total_cost / 5
    result = cost_per_person
    return result

print(solution())