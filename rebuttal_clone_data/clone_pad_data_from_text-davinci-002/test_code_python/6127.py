def solution():
    thickness = 3
    num_foldings = 4
    thickness_doubled = thickness * 2
    for i in range(num_foldings):
        thickness = thickness_doubled
    result = thickness
    return result

print(solution())