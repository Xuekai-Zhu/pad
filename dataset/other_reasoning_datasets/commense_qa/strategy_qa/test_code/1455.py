def solution():
    servings_per_turkey = 12
    serving_size = 1
    turkey_weight = servings_per_turkey * serving_size
    time_to_eat = 60 # minutes
    if turkey_weight <= 12:
        result = "maybe"
    else:
        result = "no"
    return result

print(solution())