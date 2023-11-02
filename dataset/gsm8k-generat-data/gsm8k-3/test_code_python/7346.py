def solution():
    """Penelope has 5 M&M candies for every 3 Starbursts candies. If she has 25 M&M candies, how many Starbursts candies does she have?"""
    # Define the ratio of M&M candies to Starbursts candies
    MM_TO_SB_RATIO = 5 / 3

    # Define the number of M&M candies Penelope has
    num_mm = 25

    # Calculate the number of Starbursts candies Penelope has
    num_sb = num_mm / MM_TO_SB_RATIO

    # Display the number of Starbursts candies Penelope has
    result = num_sb
    return result

print(solution())