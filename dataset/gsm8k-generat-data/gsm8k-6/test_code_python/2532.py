def solution():
    # Calculate the total number of cans Kaiden needs to collect
    total_cans = 500
    cans_collected = 158 + 259  # cans collected during the first and second week
    cans_left = total_cans - cans_collected
    result = cans_left
    return result

print(solution())