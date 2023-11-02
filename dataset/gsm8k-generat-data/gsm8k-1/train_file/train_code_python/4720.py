def solution():
    """In 6 years, Carla will be 30 years old. The sum of the current ages of Carla and Louis is 55.
    How old is Louis now?"""
    carla_in_6_years = 30
    combined_current_age = 55
    carla_current_age = (carla_in_6_years - 6)
    louis_current_age = combined_current_age - carla_current_age
    result = louis_current_age
    return result

print(solution())