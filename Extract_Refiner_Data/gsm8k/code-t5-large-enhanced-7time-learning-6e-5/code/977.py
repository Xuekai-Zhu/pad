def solution():
    
    thursday_catch = 3
    friday_catch = 4 * thursday_catch
    saturday_catch = friday_catch / 2
    total_catch = thursday_catch + friday_catch + saturday_catch
    serving_size = 3
    total_servings = total_catch / serving_size
    result = total_servings
    return result

print(solution())