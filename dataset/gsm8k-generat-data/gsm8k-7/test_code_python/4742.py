def solution():
    num_parents = 2
    num_brothers = 3
    num_brother_spouses = 3 # each brother has a spouse
    num_nephews_nieces = 6 # each brother has 2 children

    num_relatives = num_parents + num_brothers + num_brother_spouses + num_nephews_nieces

    cost_per_package = 5
    total_cost = cost_per_package * num_relatives
    result = total_cost
    return result

print(solution())