def solution():
    """Each member of Greg’s softball team needs to buy one uniform made up of a shirt, a pair of pants, and socks. A shirt costs $7.50, a pair of pants cost $15, and socks cost $4.50 each if each team member buys the uniform items on their own. If they buy the items as a group, they are given a discount. A discounted shirt cost $6.75, a discounted pair of pants cost $13.50, and discounted socks cost $3.75. How much would their team of 12 save with the group discount?"""
    num_team_members = 12
    individual_shirt_cost = 7.5
    individual_pants_cost = 15
    individual_socks_cost = 4.5
    discount_shirt_cost = 6.75
    discount_pants_cost = 13.5
    discount_socks_cost = 3.75
    individual_uniform_cost = individual_shirt_cost + individual_pants_cost + individual_socks_cost
    discounted_uniform_cost = discount_shirt_cost + discount_pants_cost + discount_socks_cost
    savings_per_person = individual_uniform_cost - discounted_uniform_cost
    total_savings = savings_per_person * num_team_members
    result = total_savings
    return result

print(solution())