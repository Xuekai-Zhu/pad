def solution():
    # Calculate the total number of people in Andrew's family
    total_people = 1 + 2 + 2

    # Calculate the number of masks used by the family each day
    masks_per_day = total_people * (1 / 4)

    # Calculate the total number of days the masks will last
    total_days = 100 / masks_per_day
    result = total_days
    return result

print(solution())