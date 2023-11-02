def solution():
    """Rose bought her mother one dozen flowers. Two of the flowers are daisies. Three-fifths of the remaining flowers are tulips and the rest are sunflowers. How many sunflowers are there?"""
    # Define the number of flowers in a dozen and the number of daisies
    DOZEN = 12
    DAISIES = 2

    # Calculate the number of remaining flowers
    remaining_flowers = DOZEN - DAISIES

    # Calculate the number of tulips
    tulips = remaining_flowers * 3 / 5

    # Calculate the number of sunflowers
    sunflowers = remaining_flowers - tulips

    # Display the number of sunflowers
    result = sunflowers
    return result

print(solution())