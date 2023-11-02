def solution():
    """Tim buys 3 loaves of bread. Each loaf of bread has 20 slices. He pays for the 3 loaves of bread with 2 $20 bills. He gets $16 change. How much does each slice cost, in cents?"""
    loaves_of_bread = 3
    slices_per_loaf = 20
    total_slices = loaves_of_bread * slices_per_loaf
    total_cost = 2*20 + 16
    cost_per_slice = total_cost * 100 // total_slices
    result = cost_per_slice
    return result

print(solution())