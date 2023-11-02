def solution():
    # Calculate the total distance Jim runs in the first 30 days
    distance_first_month = 5 * 30  # Jim runs 5 miles every day for 30 days

    # Calculate the total distance Jim runs in the second 30 days
    distance_second_month = 10 * 30  # Jim runs 10 miles every day for 30 days

    # Calculate the total distance Jim runs in the last 30 days
    distance_third_month = 20 * 30  # Jim runs 20 miles every day for 30 days

    # Calculate the total distance Jim runs in 90 days
    total_distance = distance_first_month + distance_second_month + distance_third_month
    result = total_distance
    return result

print(solution())