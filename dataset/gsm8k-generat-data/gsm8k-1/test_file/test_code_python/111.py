def solution():
    """Sasha notices that prices for lumber have gone up 50% in the last few months after she bought some lumber. Since she has leftovers, she decides to sell them. She has leftover ten 2 x 4 x 10 boards that cost her $10 each. She also has five 4 x 4 x 10 boards she bought for $16 each. If she sells them all, how much profit does she make?"""
    num_2x4x10 = 10
    num_4x4x10 = 5
    cost_2x4x10 = 10
    cost_4x4x10 = 16
    percent_increase = 50
    increase_factor = 1 + (percent_increase / 100)
    new_cost_2x4x10 = cost_2x4x10 * increase_factor
    new_cost_4x4x10 = cost_4x4x10 * increase_factor
    revenue_2x4x10 = num_2x4x10 * new_cost_2x4x10
    revenue_4x4x10 = num_4x4x10 * new_cost_4x4x10
    total_revenue = revenue_2x4x10 + revenue_4x4x10
    total_cost = (num_2x4x10 * cost_2x4x10) + (num_4x4x10 * cost_4x4x10)
    profit = total_revenue - total_cost
    result = profit
    return result

print(solution())