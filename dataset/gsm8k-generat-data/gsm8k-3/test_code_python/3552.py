def solution():
    """There are 60 ridges on a vinyl record. Jerry has 4 cases, each with 3 shelves that can hold 20 records each. If his shelves are 60% full, how many ridges are there on all his records?"""
    # Define the number of ridges per record
    RIDGES_PER_RECORD = 60

    # Define the number of cases, shelves, and records per shelf
    num_cases = 4
    num_shelves = 3
    records_per_shelf = 20

    # Calculate the total number of shelves
    total_shelves = num_cases * num_shelves

    # Calculate the total number of records
    total_records = total_shelves * records_per_shelf * 0.6

    # Calculate the total number of ridges
    total_ridges = total_records * RIDGES_PER_RECORD

    # Display the total number of ridges
    result = total_ridges
    return result

print(solution())