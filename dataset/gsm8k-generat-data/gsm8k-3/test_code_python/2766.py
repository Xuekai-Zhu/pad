def solution():
    """Lara bought 52 stems of flowers at the flower shop. She gave 15 flowers to her mom and gave 6 more flowers than she gave to her mom to her grandma. She put the rest in a vase. How many stems of flowers did Lara put in the vase?"""
    # Define the number of flowers Lara gave to her mom and the number she gave to her grandma
    mom_flowers = 15
    grandma_flowers = mom_flowers + 6

    # Calculate the total number of flowers Lara gave away
    total_given = mom_flowers + grandma_flowers

    # Calculate the number of flowers Lara put in the vase
    vase_flowers = 52 - total_given

    # Display the number of flowers in the vase
    result = vase_flowers
    return result

print(solution())