def solution():
    red_tulips_for_eyes = 8 * 2  # Anna needs 8 red tulips for each of the 2 eyes
    red_tulips_for_smile = 18  # Anna needs 18 red tulips for the smile
    yellow_tulips_for_background = 9 * red_tulips_for_smile  # Anna needs 9 times the number of red tulips for the smile for the yellow background
    total_tulips = red_tulips_for_eyes + red_tulips_for_smile + yellow_tulips_for_background
    result = total_tulips
    return result

print(solution())