def solution():
    batches = 4
    minutes_to_bake = 20
    minutes_to_ice = 30
    total_minutes = (batches * minutes_to_bake) + (batches * minutes_to_ice)
    result = total_minutes
    return result

print(solution())