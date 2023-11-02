def solution():
    total_miles = 493  # Total miles driven for the three-day trip
    miles_day_1 = 125  # Miles driven on the first day
    miles_day_2 = 223  # Miles driven on the second day

    # Calculate the miles driven on the third day
    miles_day_3 = total_miles - miles_day_1 - miles_day_2
    result = miles_day_3
    return result

print(solution())