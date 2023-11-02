def solution():
    peppers_per_very_spicy = 3
    peppers_per_spicy = 2
    peppers_per_mild = 1

    # Calculate the total number of peppers previously purchased
    prev_peppers = 30 * peppers_per_very_spicy + 30 * peppers_per_spicy + 10 * peppers_per_mild

    # Calculate the total number of peppers now purchased
    new_peppers = 15 * peppers_per_spicy + 90 * peppers_per_mild

    # Calculate the difference in peppers bought
    pepper_difference = prev_peppers - new_peppers
    result = pepper_difference
    return result

print(solution())