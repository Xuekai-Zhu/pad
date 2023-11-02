def solution():
    mother_age_when_she_died = 70 - 10  # Mother would be 70 years old if alive now
    jessica_age_at_time_of_death = mother_age_when_she_died / 2
    jessica_current_age = jessica_age_at_time_of_death + 10  # 10 years have passed since her mother would have been 70
    result = jessica_current_age
    return result

print(solution())