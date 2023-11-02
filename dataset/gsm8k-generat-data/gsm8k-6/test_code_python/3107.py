def solution():
    # Calculate the total number of hours both Cathy and Chris were supposed to work
    total_hours = 20 * 2 * 4  # 20 hours per week each for 2 months (4 weeks in a month)

    # Calculate the number of hours Chris was unable to work
    sick_hours = 20 * 1  # Chris was sick for one week, so 20 hours missed

    # Calculate the number of hours Cathy worked during the 2 months
    cathy_hours = total_hours + sick_hours - (20 * 3)  # Cathy covered Chris's shift for one week (20 hours), and she was already working 20 hours per week
    result = cathy_hours
    return result

print(solution())