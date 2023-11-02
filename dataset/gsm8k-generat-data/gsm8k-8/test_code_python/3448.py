def solution():
    # Calculate the number of towel pairs Barney uses per week
    towel_pairs_per_week = 7 * 2 / 7

    # Calculate the number of towel pairs Barney missed washing
    missed_towel_pairs = 2

    # Calculate the number of towel pairs Barney has left for the following week
    remaining_towel_pairs = 18 / 2 - missed_towel_pairs

    # Calculate the number of days Barney will not have clean towels
    days_without_clean_towels = missed_towel_pairs + remaining_towel_pairs * 7

    result = days_without_clean_towels
    return result

print(solution())