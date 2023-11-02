def solution():
    num_bottles = 5
    stars_per_bottle = 15

    # Calculate the total number of stars that can be held in the two original bottles
    num_stars = num_bottles // 2 * stars_per_bottle

    # Calculate the total number of stars needed to fill all the bottles
    total_stars_needed = num_bottles * stars_per_bottle

    # Calculate the number of stars Kyle needs to make
    num_stars_to_make = total_stars_needed - num_stars
    result = num_stars_to_make
    return result

print(solution())