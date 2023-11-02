def solution():
    total_flour = 200 + 100 + 100  # Jim has 200g of flour in the cupboard, 100g on the counter, and 100g in the pantry
    flour_per_loaf = 200  # One loaf of bread requires 200g of flour

    # Calculate the number of loaves Jim can bake
    num_loaves = total_flour // flour_per_loaf
    result = num_loaves
    return result

print(solution())