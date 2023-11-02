def solution():
    """In twenty years, Ramon will be twice as old as Loui today. If Loui is currently 23 years old, how old is Ramon now?"""
    loui_age = 23
    ramon_age_in_twenty_years = 2 * loui_age
    ramon_current_age = ramon_age_in_twenty_years - 20
    result = ramon_current_age
    return result

print(solution())