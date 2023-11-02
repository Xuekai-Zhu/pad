def solution():
    # Calculate the total number of miles and stop signs encountered
    total_miles = 5 + 2  # Rudolph traveled 2 more than 5 miles
    total_stop_signs = 17 - 3  # Rudolph encountered 3 less than 17 stop signs

    # Calculate the number of stop signs per mile
    stop_signs_per_mile = total_stop_signs / total_miles
    result = stop_signs_per_mile
    return result

print(solution())