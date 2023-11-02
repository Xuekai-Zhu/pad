def solution():
    # Define the number of daisies and total flowers
    daisies = 2
    total_flowers = 12

    # Calculate the number of non-daisy flowers
    non_daisy_flowers = total_flowers - daisies

    # Calculate the number of tulips
    tulips = 3/5 * non_daisy_flowers

    # Calculate the number of sunflowers
    sunflowers = non_daisy_flowers - tulips

    result = sunflowers
    return result

print(solution())