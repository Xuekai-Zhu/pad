def solution():
    troy_distance = 75 * 2  # Troy walks 75 meters to school and 75 meters back home per day
    emily_distance = 98 * 2  # Emily walks 98 meters to school and 98 meters back home per day
    days = 5  # Troy and Emily walk to school and back home for 5 days

    # Calculate the total distance Emily walks in five days
    total_emily_distance = emily_distance * days

    # Calculate the total distance Troy walks in five days
    total_troy_distance = troy_distance * days

    # Calculate how much farther Emily walks in five days compared to Troy
    extra_distance = total_emily_distance - total_troy_distance
    result = extra_distance
    return result

print(solution())