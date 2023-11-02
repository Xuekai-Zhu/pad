def solution():
    karen_age = 2
    carla_age = karen_age + 2
    ty_age = (carla_age * 2) + 4
    frank_age_5_years_from_now = (ty_age + 5) * 3

    # Calculate Frank's current age
    frank_age = frank_age_5_years_from_now - 5
    result = frank_age
    return result

print(solution())