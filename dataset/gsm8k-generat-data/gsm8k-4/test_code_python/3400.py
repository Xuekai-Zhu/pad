def solution():
    """Rodney, Roger and Ron can lift a combined weight of 239 pounds. Rodney can lift twice as much as Roger, and Roger can lift 7 pounds less than 4 times the amount that Ron can lift. How much can Rodney lift?"""
    # Define the combined weight lifted by all three
    total_weight = 239

    # Let's assume Ron can lift x pounds
    # Then Roger can lift 4x - 7 pounds
    # And Rodney can lift 2 * (4x - 7) = 8x - 14 pounds
    x = total_weight / (4 + 2 + 1)
    roger_weight = 4 * x - 7
    rodney_weight = 8 * x - 14

    # Return the weight Rodney can lift
    result = rodney_weight
    return result

print(solution())