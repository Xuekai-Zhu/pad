def solution():
    """Rose bought her mother one dozen flowers. Two of the flowers are daisies. Three-fifths of the remaining flowers are tulips and the rest are sunflowers. How many sunflowers are there?"""
    # Define the initial number of flowers
    initial_flowers = 12

    # Calculate the number of remaining flowers after removing the daisies
    remaining_flowers = initial_flowers - 2

    # Calculate the number of tulips
    tulip_flowers = remaining_flowers * 3/5

    # Calculate the number of sunflowers
    sunflower_flowers = remaining_flowers - tulip_flowers

    # Return the result
    result = sunflower_flowers
    return result

print(solution())