def solution():
    cartons = 3
    scoops_per_carton = 10
    number_scoops = 3*scoops_per_carton
    number_scoops_used = 1 + 1 + 2 + 2 + 2 + 2
    number_scoops_left = number_scoops - number_scoops_used
    result = number_scoops_left

    return result

print(solution())