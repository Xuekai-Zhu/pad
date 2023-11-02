def solution():
    """There are 60 ridges on a vinyl record. Jerry has 4 cases, each with 3 shelves that can hold 20 records each. If his shelves are 60% full, how many ridges are there on all his records?"""
    total_cases = 4
    shelves_per_case = 3
    records_per_shelf = 20
    total_records = total_cases * shelves_per_case * records_per_shelf * 0.6
    total_ridges = total_records * 60
    result = total_ridges
    return result

print(solution())