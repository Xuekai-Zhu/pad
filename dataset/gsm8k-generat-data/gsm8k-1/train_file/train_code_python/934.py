def solution():
    """Jim is baking loaves of bread. He has 200g of flour in the cupboard, 100g of flour on the kitchen counter, and 100g in the pantry. If one loaf of bread requires 200g of flour, how many loaves can Jim bake?"""
    total_flour = 200 + 100 + 100
    flour_per_loaf = 200
    loaves = total_flour // flour_per_loaf
    result = loaves
    return result

print(solution())