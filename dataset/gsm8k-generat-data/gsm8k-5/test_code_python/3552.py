def solution():
    total_shelves = 4 * 3  # Jerry has a total of 12 shelves
    records_per_shelf = 20  # Each shelf can hold 20 records
    full_percentage = 0.6  # Jerry's shelves are 60% full

    # Calculate the total number of records Jerry has
    total_records = total_shelves * records_per_shelf / full_percentage

    # Calculate the total number of ridges on Jerry's records
    total_ridges = total_records * 60
    result = total_ridges
    return result

print(solution())