def solution():
    apples_on_tuesday = 4
    apples_on_wednesday = 2*apples_on_tuesday
    apples_on_thursday = 0.5*apples_on_tuesday

    total_apples = apples_on_tuesday + apples_on_wednesday + apples_on_thursday
    result = total_apples
    return result

print(solution())