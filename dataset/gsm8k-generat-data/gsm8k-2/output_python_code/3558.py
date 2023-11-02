def solution():
    """Tim buys 3 loaves of bread. Each loaf of bread has 20 slices. He pays for the 3 loaves of bread with 2 $20 bills. He gets $16 change. How much does each slice cost, in cents?"""
    num_slices = 3 * 20
    total_cost = 2 * 20 + 16
    cost_per_slice = (total_cost * 100) / num_slices
    result = cost_per_slice
    return result

print(solution())