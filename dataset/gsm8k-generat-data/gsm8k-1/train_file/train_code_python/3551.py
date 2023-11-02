def solution():
    """There are 60 ridges on a vinyl record. Jerry has 4 cases, each with 3 shelves that can hold 20 records each. If his shelves are 60% full, how many ridges are there on all his records?"""
    ridges_per_record = 60
    cases = 4
    shelves_per_case = 3
    records_per_shelf = 20
    shelf_fill_percent = 60

    total_records = cases * shelves_per_case * records_per_shelf
    total_records_filled = total_records * (shelf_fill_percent / 100)
    total_ridges = total_records_filled * ridges_per_record
    result = total_ridges
    return result

print(solution())