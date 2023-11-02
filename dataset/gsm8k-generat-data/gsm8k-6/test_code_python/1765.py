def solution():
    # Calculate the total number of worms needed to feed the babies for 3 days
    total_worms_needed = 6 * 3 * 3  # 6 babies, 3 worms each, for 3 days = 54 worms

    # Calculate the total number of worms Mama bird currently has
    total_worms = 9 + 13 - 2  # Papa bird caught 9, Mama caught 13 but 2 were stolen = 20 worms

    # Calculate how many more worms Mama bird needs to catch
    worms_to_catch = total_worms_needed - total_worms
    result = worms_to_catch
    return result

print(solution())