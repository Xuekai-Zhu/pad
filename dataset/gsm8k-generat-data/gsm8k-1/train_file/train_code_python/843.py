def solution():
    """In 5 years, Andy will be twice as old as Rahim is now. Rahim is 6 now. How much older is Andy than Rahim, right now, in years?"""
    current_age_rahim = 6
    years_to_add = 5
    current_age_andy = 2 * (current_age_rahim + years_to_add) - years_to_add
    age_difference = current_age_andy - current_age_rahim
    result = age_difference
    return result

print(solution())