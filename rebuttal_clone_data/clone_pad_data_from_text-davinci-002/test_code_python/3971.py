def solution():
    total_miles_biked = 30
    miles_biked_on_wednesday = 12
    miles_biked_on_saturday = 2 * (total_miles_biked - miles_biked_on_wednesday)
    result = miles_biked_on_saturday / 2
    return result

print(solution())