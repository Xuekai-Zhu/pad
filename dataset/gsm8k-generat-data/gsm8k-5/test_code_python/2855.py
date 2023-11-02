def solution():
    orange_cone_price = 2.00
    icecream_sandwich_price = 1.50
    nutty_buddy_price = 3.00
    cones_per_week = 3
    sandwiches_per_week = 2
    nutty_buddies_per_week = 2
    weeks = 6
    
    # Calculate the total cost of orange creamsicles
    orange_cost = orange_cone_price * cones_per_week * weeks

    # Calculate the total cost of ice cream sandwiches
    sandwich_cost = icecream_sandwich_price * sandwiches_per_week * weeks

    # Calculate the total cost of Nutty-Buddies
    nutty_buddy_cost = nutty_buddy_price * nutty_buddies_per_week * weeks

    # Calculate the total cost of all ice cream treats
    total_cost = orange_cost + sandwich_cost + nutty_buddy_cost
    result = total_cost
    return result

print(solution())