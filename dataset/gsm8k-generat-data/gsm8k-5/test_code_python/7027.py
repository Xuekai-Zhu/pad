def solution():
    total_distance = 70  # Bob runs a total of 70 miles in the 3 days
    distance_day_one = total_distance * 0.2  # Bob runs 20% of the total distance on day one
    remaining_distance = total_distance - distance_day_one  # Bob has the remaining distance to run on day 2 and day 3
    distance_day_two = remaining_distance * 0.5  # Bob runs 50% of the remaining distance on day two
    distance_day_three = total_distance - distance_day_one - distance_day_two  # Bob runs the remaining distance on day three

    result = distance_day_three
    return result

print(solution())