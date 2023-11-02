def solution():
    # Calculate the total number of shelves Jerry has
    total_shelves = 4 * 3

    # Calculate the total number of records Jerry can store
    total_records = total_shelves * 20 * 0.6

    # Calculate the total number of ridges on all Jerry's records
    total_ridges = total_records * 60

    result = total_ridges
    return result

print(solution())