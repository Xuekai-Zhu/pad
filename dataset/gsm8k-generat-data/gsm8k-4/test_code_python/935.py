def solution():
    """Jim is baking loaves of bread. He has 200g of flour in the cupboard, 100g of flour on the kitchen counter, and 100g in the pantry. If one loaf of bread requires 200g of flour, how many loaves can Jim bake?"""
    # Define the total amount of flour Jim has
    total_flour = 200 + 100 + 100

    # Calculate the number of loaves Jim can bake
    num_loaves = total_flour // 200

    result = num_loaves
    return result

print(solution())