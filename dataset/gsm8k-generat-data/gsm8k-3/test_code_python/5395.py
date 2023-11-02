def solution():
    """Dale just learned how to make homemade macaroni and cheese. He decided to make a big batch for his family reunion. The original recipe calls for 2 pounds of pasta and serves 7 people. Dale's family reunion will have 35 people. How many pounds of pasta does Dale need to buy?"""
    # Define the original recipe's pasta-to-servings ratio
    PASTA_PER_SERVING = 2 / 7

    # Define the number of people at the family reunion
    NUM_PEOPLE = 35

    # Calculate the total amount of pasta needed
    pasta_needed = NUM_PEOPLE * PASTA_PER_SERVING

    # Display the amount of pasta needed
    result = pasta_needed
    return result

print(solution())