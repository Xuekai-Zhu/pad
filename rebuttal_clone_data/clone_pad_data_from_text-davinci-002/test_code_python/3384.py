def solution():
    days = 180
    serving_size = 2
    capsules_per_bottle = 60
    servings_per_bottle = capsules_per_bottle / serving_size
    total_servings = days * serving_size
    total_bottles = total_servings / servings_per_bottle
 
    result = total_bottles
 
    return result

print(solution())