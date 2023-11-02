def solution():
    num_weeks = 6

    # Calculate the total cost of orange creamsicles (3 times a week for 6 weeks)
    orange_creamsicle_cost = 2.0
    num_orange_creamsicles = 3 * num_weeks
    total_orange_creamsicle_cost = num_orange_creamsicles * orange_creamsicle_cost

    # Calculate the total cost of ice cream sandwiches (2 times a week for 6 weeks)
    ice_cream_sandwich_cost = 1.5
    num_ice_cream_sandwiches = 2 * num_weeks
    total_ice_cream_sandwich_cost = num_ice_cream_sandwiches * ice_cream_sandwich_cost

    # Calculate the total cost of Nutty-Buddys (2 times a week for 6 weeks)
    nutty_buddy_cost = 3.0
    num_nutty_buddys = 2 * num_weeks
    total_nutty_buddy_cost = num_nutty_buddys * nutty_buddy_cost

    # Calculate the total cost of all ice cream
    total_cost = total_orange_creamsicle_cost + total_ice_cream_sandwich_cost + total_nutty_buddy_cost
    result = total_cost
    return result

print(solution())