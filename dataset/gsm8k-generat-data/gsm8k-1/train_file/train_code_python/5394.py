def solution():
    """Dale just learned how to make homemade macaroni and cheese. He decided to make a big batch for his family reunion. The original recipe calls for 2 pounds of pasta and serves 7 people. Dale's family reunion will have 35 people. How many pounds of pasta does Dale need to buy?"""
    original_recipe_pasta = 2
    original_recipe_servings = 7
    reunion_people = 35
    pasta_needed = original_recipe_pasta * (reunion_people / original_recipe_servings)
    result = pasta_needed
    return result

print(solution())