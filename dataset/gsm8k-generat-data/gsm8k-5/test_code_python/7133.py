def solution():
    # Calculate the total number of apples collected
    total_apples = 60 + (2*4) + 7  # 60 apples left + 2 children ate 4 each + 1 child sold 7

    # Calculate the number of children
    children = total_apples / 15

    result = children
    return result

print(solution())