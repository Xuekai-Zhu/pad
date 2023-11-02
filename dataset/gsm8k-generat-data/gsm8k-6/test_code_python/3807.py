def solution():
    # Calculate the total number of muffins needed for 9 months
    total_muffins = 6 * 24 * 9  # 6 muffins per batch, 24 students, 9 months
    # Calculate the number of batches needed
    num_batches = total_muffins // 6  # each batch contains 6 muffins
    result = num_batches
    return result

print(solution())