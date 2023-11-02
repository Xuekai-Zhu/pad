def solution():
    """Rodney, Roger and Ron can lift a combined weight of 239 pounds.  Rodney can lift twice as much as Roger, and Roger can lift 7 pounds less than 4 times the amount that Ron can lift.  How much can Rodney lift?"""
    # Define variables
    ron_weight = x
    roger_weight = 4 * x - 7
    rodney_weight = 2 * (4 * x - 7)

    # Set up equation
    total_weight = ron_weight + roger_weight + rodney_weight
    total_weight = 239

    # Solve for x and calculate Rodney's weight
    x = (239 + 14) / 18
    rodney_weight = 2 * (4 * x - 7)

    # Display Rodney's weight
    result = rodney_weight
    return result

print(solution())