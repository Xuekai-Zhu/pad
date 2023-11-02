def solution():
    """Shane prepares sandwiches for the Boy Scouts. He buys 2 packages of sliced bread containing 20 slices each, and he also buys 2 packages of sliced ham containing 8 slices each. Shane will make as many sandwiches as he can according to the ham he has. How many slices of bread will he have leftover?"""
    bread_slices = 2 * 20
    ham_slices = 2 * 8
    max_sandwiches = ham_slices // 2
    used_bread_slices = max_sandwiches * 2
    leftover_bread_slices = bread_slices - used_bread_slices
    result = leftover_bread_slices
    return result

print(solution())