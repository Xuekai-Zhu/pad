def solution():
    """One of the clubs at Georgia's school was selling carnations for a fundraising event. A carnation costs $0.50. They also had a special where you could buy one dozen carnations for $4.00. If Georgia sent a dozen carnations to each of her 5 teachers and bought one carnation for each of her 14 friends, how much money would she spend?"""
    single_carnation_price = 0.5
    dozen_price = 4
    num_teachers = 5
    num_friends = 14
    num_carnations = num_teachers * 12 + num_friends
    num_dozens = num_carnations // 12
    num_singles = num_carnations % 12
    total_price = num_dozens * dozen_price + num_singles * single_carnation_price
    result = total_price
    return result

print(solution())