def solution():
    shelves_per_case = 3
    cases = 4
    records_per_shelf = 20
    total_shelves = shelves_per_case * cases
    total_records = total_shelves * records_per_shelf
    percent_full = 60
    ridges_per_record = 60
    total_ridges = total_records * ridges_per_record * (percent_full / 100)
    result = total_ridges
    return result

print(solution())