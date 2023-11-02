def solution():
    total_flowers = 6 * 13  # total number of flowers in Wilma's garden
    yellow_flowers = 12  # given
    green_flowers = 2 * yellow_flowers  # given
    red_flowers = total_flowers - yellow_flowers - green_flowers  # remaining flowers
    result = red_flowers
    return result

print(solution())