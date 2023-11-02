def solution():
    """On a four-day trip, Carrie drove 135 miles the first day, 124 miles more the second day, 159 miles the third day, and 189 miles the fourth day. If she had to charge her phone every 106 miles, how many times did she charge her phone for the whole trip?"""
    # Define the distances driven on each day
    day1_distance = 135
    day2_distance = 135 + 124
    day3_distance = 135 + 124 + 159
    day4_distance = 135 + 124 + 159 + 189

    # Calculate the total distance driven
    total_distance = day1_distance + day2_distance + day3_distance + day4_distance

    # Calculate the number of times Carrie charged her phone
    phone_charges = total_distance // 106

    result = phone_charges
    return result

print(solution())