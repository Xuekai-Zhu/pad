def solution():
    # Calculate the total cost of each item ordered
    cost_taco_salad = 10
    cost_hamburger = 5 * 5
    cost_french_fries = 4 * 2.5
    cost_peach_lemonade = 5 * 2

    # Calculate the total cost of the bill
    total_cost = cost_taco_salad + cost_hamburger + cost_french_fries + cost_peach_lemonade

    # Calculate the amount each person needs to pay
    num_people = 5
    amount_per_person = total_cost / num_people

    result = amount_per_person
    return result

print(solution())