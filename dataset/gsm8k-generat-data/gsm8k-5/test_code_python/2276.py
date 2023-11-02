def solution():
    original_volume = 6 * 4  # Billy starts with 6 quarts of juice, which is 24 cups
    reduced_volume = original_volume / 12  # He reduces the volume to 1/12 of its original volume
    final_volume = reduced_volume + 1  # He adds 1 cup of sugar to the reduced volume

    result = final_volume
    return result

print(solution())