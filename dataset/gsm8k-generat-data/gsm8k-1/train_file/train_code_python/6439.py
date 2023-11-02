def solution():
    """Each member of Greg’s softball team needs to buy one uniform made up of a shirt, a pair of pants, and socks. A shirt costs $7.50, a pair of pants cost $15, and socks cost $4.50 each if each team member buys the uniform items on their own. If they buy the items as a group, they are given a discount. A discounted shirt cost $6.75, a discounted pair of pants cost $13.50, and discounted socks cost $3.75. How much would their team of 12 save with the group discount?"""
    individual_cost = 7.5 + 15 + 4.5
    group_cost = 6.75 + 13.5 + 3.75
    per_person_savings = individual_cost - group_cost
    total_savings = per_person_savings * 12
    result = total_savings
    return result

print(solution())