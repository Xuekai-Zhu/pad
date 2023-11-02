def solution():
    # Convert row length to inches and calculate the number of 18-inch spaces available
    row_length_inches = 120 * 12  # convert row length from feet to inches
    spaces_available = row_length_inches // 18  # calculate the number of 18-inch spaces available
    result = spaces_available
    return result

print(solution())