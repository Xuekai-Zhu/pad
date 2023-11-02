def solution():
    # Calculate the total number of ice cream cones Erica buys
    total_cones = 6 * 7  # 6 weeks * 7 days/week = 42 cones

    # Calculate the total cost for the orange creamsicles
    creamsicle_cost = 2 * (3 * 2)  # 3 cones/week * $2/cone = $6/week
    creamsicle_total = creamsicle_cost * 6  # $6/week * 6 weeks = $36

    # Calculate the total cost for the ice cream sandwiches
    sandwich_cost = 1.5 * (2 * 2)  # 2 cones/week * $1.50/cone = $3/week
    sandwich_total = sandwich_cost * 6  # $3/week * 6 weeks = $18

    # Calculate the total cost for the Nutty-Buddys
    nutty_buddy_cost = 3 * (2 * 2)  # 2 cones/week * $3/cone = $6/week
    nutty_buddy_total = nutty_buddy_cost * 6  # $6/week * 6 weeks = $36

    # Calculate the total cost for all the ice cream
    total_cost = creamsicle_total + sandwich_total + nutty_buddy_total

    result = total_cost
    return result

print(solution())