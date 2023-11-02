def solution():
    """One of the clubs at Georgia's school was selling carnations for a fundraising event. A carnation costs $0.50. They also had a special where you could buy one dozen carnations for $4.00. If Georgia sent a dozen carnations to each of her 5 teachers and bought one carnation for each of her 14 friends, how much money would she spend?"""
    cost_per_carnation = 0.5
    cost_per_dozen = 4.0
    num_teachers = 5
    num_friends = 14
    num_carnations = num_teachers * 12 + num_friends
    num_dozens = num_carnations // 12
    remainder = num_carnations % 12
    total_cost = num_dozens * cost_per_dozen + remainder * cost_per_carnation
    result = total_cost
    return result

print(solution())