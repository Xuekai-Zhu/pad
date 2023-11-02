def solution():
    # Calculate the number of flowers Lara gave to her grandma
    flowers_to_grandma = 15 + 6  # Lara gave 6 more flowers to her grandma than to her mom

    # Calculate the total number of flowers not in vase
    not_in_vase = 15 + flowers_to_grandma

    # Calculate the number of flowers in vase
    in_vase = 52 - not_in_vase
    result = in_vase
    return result

print(solution())