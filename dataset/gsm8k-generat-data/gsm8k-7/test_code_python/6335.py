def solution():
    total_vegetables = 280
    tomato_ratio = 3  # three times as many tomatoes as cucumbers

    # Set up a system of equations to solve for the number of cucumbers (c) and tomatoes (t)
    # c + t = 280    (total number of vegetables)
    # t = 3c        (three times as many tomatoes as cucumbers)
    # Substitute t = 3c into the first equation and solve for c
    # c + 3c = 280
    # 4c = 280
    # c = 70

    num_cucumbers = 70
    result = num_cucumbers
    return result

print(solution())