def solution():
    """Vivian is responsible for making sure her students get 2 15-minute recess breaks a day, a 30-minute lunch and another 20-minute recess break. How much time do her students spend outside of class?"""
    recess_breaks_per_day = 2
    lunch_break = 30
    additional_recess_break = 20
    total_time_outside = (recess_breaks_per_day * 15 * 2) + lunch_break + additional_recess_break
    result = total_time_outside
    return result

print(solution())