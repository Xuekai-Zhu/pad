def solution():
    cupcakes_baked = 65
    batches = 45
    cupcakes_fed_to_dogs = 5
    left_over_cupcakes = (cupcakes_baked * batches) - (cupcakes_fed_to_dogs * batches)
    people = 19
    cupcakes_ate = left_over_cupcakes / people
    result = cupcakes_ate
    return result

print(solution())