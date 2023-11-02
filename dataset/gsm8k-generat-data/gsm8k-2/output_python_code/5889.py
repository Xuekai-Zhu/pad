def solution():
    """Laura’s House is a 20-mile round trip from her school. The supermarket is 10 miles farther away from the school. If Laura drives to school every morning and two afternoons a week drives to the supermarket. How many miles does Laura driver per week?"""
    school_distance = 20
    supermarket_distance = school_distance + 10
    morning_driving_distance = school_distance * 2
    afternoon_driving_distance = supermarket_distance * 2
    total_weekly_driving_distance = morning_driving_distance + afternoon_driving_distance
    result = total_weekly_driving_distance
    return result

print(solution())