def solution():
    
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