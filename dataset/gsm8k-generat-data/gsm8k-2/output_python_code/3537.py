def solution():
    """On a four-day trip, Carrie drove 135 miles the first day, 124 miles more the second day, 159 miles the third day, and 189 miles the fourth day. If she had to charge her phone every 106 miles, how many times did she charge her phone for the whole trip?"""
    total_miles = 135 + 259 + 159 + 189
    charge_count = total_miles // 106
    if total_miles % 106 != 0:
        charge_count += 1

    result = charge_count
    return result

print(solution())