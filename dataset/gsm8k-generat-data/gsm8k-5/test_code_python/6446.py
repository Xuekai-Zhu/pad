def solution():
    total_bottles = 24  # A family bought a 24 pack of bottled water

    # Calculate the number of bottles drank on the first day
    first_day_bottles = total_bottles / 3

    # Calculate the number of bottles left after the first day
    remaining_bottles_1 = total_bottles - first_day_bottles

    # Calculate the number of bottles drank on the second day
    second_day_bottles = remaining_bottles_1 / 2

    # Calculate the total number of bottles remaining after 2 days
    total_remaining_bottles = remaining_bottles_1 - second_day_bottles
    result = total_remaining_bottles
    return result

print(solution())