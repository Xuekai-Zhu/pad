def solution():
    """Dale just learned how to make homemade macaroni and cheese. He decided to make a big batch for his family reunion. The original recipe calls for 2 pounds of pasta and serves 7 people. Dale's family reunion will have 35 people. How many pounds of pasta does Dale need to buy?"""
    # Define the original recipe's serving size and pasta requirement
    ORIGINAL_SERVINGS = 7
    ORIGINAL_PASTA = 2

    # Define the number of people at the family reunion
    FAMILY_REUNION = 35

    # Calculate the total amount of pasta needed based on the number of servings required
    total_pasta = ORIGINAL_PASTA * (FAMILY_REUNION / ORIGINAL_SERVINGS)

    result = total_pasta
    return result

print(solution())