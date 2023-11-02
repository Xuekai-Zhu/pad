def solution():
    # Define the ratios of ingredients
    mint_ratio = 3
    tea_per_mint = 2

    # Calculate the original total number of tea leaves
    original_tea_leaves = mint_ratio * tea_per_mint

    # Calculate the new total number of tea leaves with half effectiveness
    new_tea_leaves = original_tea_leaves * 2

    result = new_tea_leaves
    return result

print(solution())