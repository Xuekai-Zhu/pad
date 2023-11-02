def solution():
    num_team_members = 12
    shirt_cost_indiv = 7.5
    pants_cost_indiv = 15
    socks_cost_indiv = 4.5

    shirt_cost_group = 6.75
    pants_cost_group = 13.5
    socks_cost_group = 3.75

    # Calculate the total cost of a uniform if each member buys individually
    total_cost_indiv = (shirt_cost_indiv + pants_cost_indiv + socks_cost_indiv)

    # Calculate the total cost of a uniform if the group buys together
    total_cost_group = (shirt_cost_group + pants_cost_group + socks_cost_group)

    # Calculate the total savings with the group discount
    total_savings = num_team_members * (total_cost_indiv - total_cost_group)

    result = total_savings
    return result

print(solution())