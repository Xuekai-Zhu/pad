def solution():
    """Jim is baking loaves of bread. He has 200g of flour in the cupboard, 100g of flour on the kitchen counter, and 100g in the pantry. If one loaf of bread requires 200g of flour, how many loaves can Jim bake?"""
    total_flour = 200 + 100 + 100
    loaf_flour = 200
    num_loaves = total_flour // loaf_flour
    result = num_loaves
    return result

print(solution())