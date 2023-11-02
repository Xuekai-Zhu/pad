def solution():
    sand_in_bucket = 2
    sandbox_depth = 2
    sandbox_width = 4
    sandbox_length = 5
    sand_per_foot = 3
    trips_to_make = ((sandbox_depth * sandbox_width * sandbox_length) / sand_per_foot) / sand_in_bucket
    water_per_trip = 3 / 4
    cost_per_bottle = 2
    money_spent = ((trips_to_make * water_per_trip) / 15) * cost_per_bottle
    money_left = 10 - money_spent
    result = money_left
    return result

print(solution())