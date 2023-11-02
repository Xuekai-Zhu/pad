def solution():
    # Calculate the total fluid Tom drinks in one day
    total_fluid = (5 * 12) + 64  # 5 cans of 12 oz soda + 64 ounces of water 

    # Calculate the total fluid Tom drinks in one week
    fluid_per_week = total_fluid * 7  # multiply total fluid per day by the number of days in a week

    result = fluid_per_week
    return result

print(solution())