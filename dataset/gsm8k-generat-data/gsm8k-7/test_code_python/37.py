def solution():
    num_hamburger = 5
    hamburger_price = 3

    num_fries_sets = 4
    fries_price = 1.2

    num_soda_cups = 5
    soda_price = 0.5

    num_spaghetti_platter = 1
    spaghetti_price = 2.7

    num_friends = 5

    # Calculate the total cost of all items
    total_cost = (num_hamburger*hamburger_price)+(num_fries_sets*fries_price)+(num_soda_cups*soda_price)+(num_spaghetti_platter*spaghetti_price)

    # Calculate the cost per person
    cost_per_person = total_cost / num_friends
    result = cost_per_person
    return result

print(solution())