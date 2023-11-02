def solution():
    total_crayons = 48
    crayons_taken_by_kiley = total_crayons / 4
    crayons_left = total_crayons - crayons_taken_by_kiley
    crayons_taken_by_joe = crayons_left / 2
    crayons_left = crayons_left - crayons_taken_by_joe
    result = crayons_left
    return result

print(solution())