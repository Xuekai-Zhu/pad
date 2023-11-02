def solution():
    """Jim is baking loaves of bread. He has 200g of flour in the cupboard, 100g of flour on the kitchen counter, and 100g in the pantry. If one loaf of bread requires 200g of flour, how many loaves can Jim bake?"""
    # Define the total amount of flour Jim has
    total_flour = 200 + 100 + 100

    # Define the amount of flour needed per loaf
    flour_per_loaf = 200

    # Calculate the maximum number of loaves Jim can bake
    max_loaves = total_flour // flour_per_loaf

    # Display the maximum number of loaves Jim can bake
    result = max_loaves
    return result

print(solution())