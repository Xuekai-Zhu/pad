def solution():
    bottles_per_case = 24
    num_cases = 13
    num_days = 3

    group1_children = 14
    group2_children = 16
    group3_children = 12
    group4_children = (group1_children + group2_children + group3_children) / 2

    total_children = group1_children + group2_children + group3_children + group4_children

    total_bottles_needed = total_children * 3 * num_days

    total_bottles_available = bottles_per_case * num_cases

    bottles_needed = total_bottles_needed - total_bottles_available
    result = bottles_needed
    return result

print(solution())