def solution():
    num_cases = 4
    num_shelves_per_case = 3
    num_records_per_shelf = 20
    shelf_capacity_percentage = 0.6  # 60% full

    # Calculate the total number of records Jerry can store
    total_records_capacity = num_cases * num_shelves_per_case * num_records_per_shelf
    # Calculate the total number of records Jerry has
    total_records = total_records_capacity * shelf_capacity_percentage

    # Calculate the total number of ridges on all the records
    num_ridges = total_records * 60

    result = num_ridges
    return result

print(solution())