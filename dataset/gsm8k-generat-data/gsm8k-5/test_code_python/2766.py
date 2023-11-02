def solution():
    total_flowers = 52  # Lara bought 52 stems of flowers
    flowers_to_mom = 15  # Lara gave 15 flowers to her mom
    flowers_to_grandma = flowers_to_mom + 6  # Lara gave 6 more flowers to her grandma than to her mom

    # Calculate the total flowers given away
    flowers_given_away = flowers_to_mom + flowers_to_grandma

    # Calculate the number of flowers left in the vase
    flowers_in_vase = total_flowers - flowers_given_away
    result = flowers_in_vase
    return result

print(solution())