def solution():
    # Calculate the total amount of flour Jim has
    total_flour = 200 + 100 + 100  # 200g in the cupboard, 100g on the counter, 100g in the pantry

    # Calculate the number of loaves Jim can bake
    num_loaves = total_flour // 200  # each loaf requires 200g of flour

    result = num_loaves
    return result

print(solution())