def solution():
    carla_age_in_6_years = 30
    current_total_age = 55

    # Calculate Carla's current age
    carla_current_age = carla_age_in_6_years - 6

    # Calculate Louis' current age
    louis_current_age = current_total_age - carla_current_age

    result = louis_current_age
    return result

print(solution())