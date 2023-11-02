def solution():
    kylie_towels = 3
    daughters_towels = 6
    husband_towels = 3

    total_towels = kylie_towels + daughters_towels + husband_towels

    towels_per_load = 4

    loads_of_laundry = total_towels // towels_per_load + int(total_towels % towels_per_load > 0)

    result = loads_of_laundry
    return result

print(solution())