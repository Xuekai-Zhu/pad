def solution():
    taco_salad_price = 10
    num_hamburgers = 5
    hamburger_price = 5
    num_fries_sets = 4
    fries_price = 2.5
    num_lemonades = 5
    lemonade_price = 2

    # Calculate the total cost of all items
    total_cost = taco_salad_price + (num_hamburgers * hamburger_price) + (num_fries_sets * fries_price) + \
                 (num_lemonades * lemonade_price)

    # Calculate the cost per person
    cost_per_person = total_cost / 5
    result = cost_per_person
    return result

print(solution())