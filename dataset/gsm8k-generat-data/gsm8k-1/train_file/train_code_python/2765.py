def solution():
    """Lara bought 52 stems of flowers at the flower shop. She gave 15 flowers to her mom and gave 6 more flowers than she gave to her mom to her grandma. She put the rest in a vase. How many stems of flowers did Lara put in the vase?"""
    total_flowers = 52
    flowers_given_to_mom = 15
    flowers_given_to_grandma = flowers_given_to_mom + 6
    flowers_in_vase = total_flowers - (flowers_given_to_mom + flowers_given_to_grandma)
    result = flowers_in_vase
    return result

print(solution())