def solution():
    # Calculate how much butter can be used
    max_butter = 2 * 6  # 2 ounces of butter for every 1 cup of baking mix

    # Calculate how much coconut oil needs to be used
    remaining_mix = 6 - (4 / 2)  # remaining cups of mix after using up 4 ounces of butter
    coconut_oil = 2 * remaining_mix  # allow 2 ounces of coconut oil to be substituted for every 2 ounces of butter needed

    result = coconut_oil
    return result

print(solution())