def solution():
    num_students = 24
    muffins_per_batch = 6
    num_months = 9

    # Calculate the total number of muffins Georgia needs to make
    total_muffins = num_students * num_months

    # Calculate the total number of batches of muffins Georgia needs to make
    num_batches = total_muffins // muffins_per_batch

    result = num_batches
    return result

print(solution())