def solution():
    num_boys = 40
    num_girls = 3 * num_boys

    total_children = num_boys + num_girls

    counselors_needed = total_children // 8
    if total_children % 8 > 0:
        counselors_needed += 1

    result = counselors_needed
    return result

print(solution())