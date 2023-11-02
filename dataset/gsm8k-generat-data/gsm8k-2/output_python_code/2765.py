def solution():
    """Lara bought 52 stems of flowers at the flower shop. She gave 15 flowers to her mom and gave 6 more flowers than she gave to her mom to her grandma. She put the rest in a vase. How many stems of flowers did Lara put in the vase?"""
    total_flowers = 52
    mom_flowers = 15
    grandma_flowers = mom_flowers + 6
    remaining_flowers = total_flowers - mom_flowers - grandma_flowers
    result = remaining_flowers
    return result

print(solution())