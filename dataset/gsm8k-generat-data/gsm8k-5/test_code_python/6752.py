def solution():
    apples_per_dozen = 12  # There are 12 apples in a dozen
    total_apples = 4 * 4 * apples_per_dozen  # Cassandra bought 4 dozen apples and used them to make 4 pies
    total_slices = 4 * 6  # Each pie was cut into 6 slices

    # Calculate the number of apples in each slice of pie
    apples_per_slice = total_apples / total_slices
    result = apples_per_slice
    return result

print(solution())