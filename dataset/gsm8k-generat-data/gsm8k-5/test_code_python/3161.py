def solution():
    # Calculate the total number of eggs collected
    total_eggs = 4 + 3 + 2 + 2  # 4 from Gertrude, 3 from Blanche, 2 each from Nancy and Martha

    # Calculate the number of eggs dropped
    eggs_dropped = 2

    # Calculate the number of eggs Trevor has left
    eggs_left = total_eggs - eggs_dropped
    result = eggs_left
    return result

print(solution())