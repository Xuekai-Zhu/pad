def solution():
    num_babies = 6  # Mama bird has 6 babies in the nest
    worms_per_baby_per_day = 3  # Mama bird needs to feed each baby 3 worms a day
    worms_caught_by_papa = 9  # Papa bird caught 9 worms
    worms_caught_by_mama = 13  # Mama bird caught 13 worms
    worms_stolen = 2  # 2 worms were stolen from Mama bird

    # Calculate the total number of worms Mama bird has
    total_worms = (worms_caught_by_papa + worms_caught_by_mama - worms_stolen) * 3   # We multiply by 3 since there are 3 days

    # Calculate the total number of worms needed for 3 days
    total_worms_needed = num_babies * worms_per_baby_per_day * 3  # 3 days

    # Calculate the number of worms Mama bird needs to catch
    worms_to_catch = total_worms_needed - total_worms
    result = worms_to_catch
    return result

print(solution())