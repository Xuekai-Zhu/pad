def solution():
    """On a four-day trip, Carrie drove 135 miles the first day, 124 miles more the second day, 159 miles the third day, and 189 miles the fourth day. If she had to charge her phone every 106 miles, how many times did she charge her phone for the whole trip?"""
    total_distance = 135 + 259 + 159 + 189
    times_charging = total_distance // 106
    result = times_charging
    return result

print(solution())