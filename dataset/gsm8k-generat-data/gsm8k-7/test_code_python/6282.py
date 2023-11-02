def solution():
    capacity = 6 * 12  # in inches
    drainage_per_day = 3  # in inches
    total_rain = 0

    # day 1
    total_rain += 10

    # day 2
    total_rain += 2 * 10

    # day 3
    total_rain += 1.5 * 2 * 10

    # calculate how much space is left before the fourth day
    space_left = capacity - total_rain

    # if there is no space left, it has already flooded
    if space_left <= 0:
        return 0

    # calculate how much more rain can be handled on the fourth day
    available_rain = space_left + drainage_per_day * 3

    # calculate the minimum amount it rained on the fourth day
    fourth_day_rain = available_rain - space_left

    return fourth_day_rain

print(solution())