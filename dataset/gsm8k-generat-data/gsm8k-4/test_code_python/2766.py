def solution():
    """Lara bought 52 stems of flowers at the flower shop. She gave 15 flowers to her mom and gave 6 more flowers than she gave to her mom to her grandma. She put the rest in a vase. How many stems of flowers did Lara put in the vase?"""
    # Define the initial number of stems
    stems = 52

    # Subtract the number of stems given to Lara's mom
    stems -= 15

    # Calculate the number of stems given to Lara's grandma
    grandma_stems = 15 + 6
    stems -= grandma_stems

    # The remaining stems are put in the vase
    result = stems
    return result

print(solution())