def solution():
    """Carter usually bakes 6 cheesecakes, 5 muffins, and 8 red velvet cakes regularly for a week.
    For this week he was able to bake triple the number of cheesecakes, muffins, chocolate moist cakes, and red velvet cakes.
    How much more cakes was Carter able to bake for this week?"""
    # Define the regular number of cheesecakes, muffins, and red velvet cakes
    REGULAR_CHEESECAKES = 6
    REGULAR_MUFFINS = 5
    REGULAR_RED_VELVET = 8

    # Triple the regular number of cakes
    TRIPLE_CHEESECAKES = REGULAR_CHEESECAKES * 3
    TRIPLE_MUFFINS = REGULAR_MUFFINS * 3
    TRIPLE_RED_VELVET = REGULAR_RED_VELVET * 3

    # Calculate the difference between regular and tripled amount
    CHEESECAKES_DIFF = TRIPLE_CHEESECAKES - REGULAR_CHEESECAKES
    MUFFINS_DIFF = TRIPLE_MUFFINS - REGULAR_MUFFINS
    RED_VELVET_DIFF = TRIPLE_RED_VELVET - REGULAR_RED_VELVET

    # Calculate the total difference
    total_diff = CHEESECAKES_DIFF + MUFFINS_DIFF + RED_VELVET_DIFF

    # Display the total difference
    result = total_diff
    return result

print(solution())