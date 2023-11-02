def solution():
    """There are 60 ridges on a vinyl record. Jerry has 4 cases, each with 3 shelves that can hold 20 records each. If his shelves are 60% full, how many ridges are there on all his records?"""
    # Define the number of ridges on each record
    ridges_per_record = 60

    # Define the number of cases and shelves
    cases = 4
    shelves_per_case = 3

    # Define the maximum number of records that can be stored
    max_records_per_shelf = 20
    max_records = max_records_per_shelf * shelves_per_case * cases

    # Define the percentage of shelves that are full
    percentage_full = 0.6

    # Calculate the actual number of records that are stored
    actual_records = round(max_records * percentage_full)

    # Calculate the total number of ridges on all the records
    total_ridges = actual_records * ridges_per_record

    # return the result
    result = total_ridges
    return result

print(solution())