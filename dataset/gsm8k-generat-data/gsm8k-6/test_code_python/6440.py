def solution():
    # Calculate the cost of each item without the group discount
    shirt_cost = 7.50
    pants_cost = 15
    socks_cost = 4.50

    # Calculate the cost of each item with the group discount
    discounted_shirt_cost = 6.75
    discounted_pants_cost = 13.50
    discounted_socks_cost = 3.75

    # Calculate the total cost for each team member without the group discount
    individual_cost = shirt_cost + pants_cost + socks_cost

    # Calculate the total cost for each team member with the group discount
    group_cost = discounted_shirt_cost + discounted_pants_cost + discounted_socks_cost

    # Calculate the amount the team would save with the group discount
    total_savings = (individual_cost - group_cost) * 12
    result = total_savings
    return result

print(solution())