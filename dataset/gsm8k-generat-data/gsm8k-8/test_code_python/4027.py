def solution():
    # Calculate maximum number of cheesecakes Lionel can make
    max_cheesecakes = min(14//2, 15//3)

    # Calculate how many ingredients he used for the cheesecakes
    used_graham_crackers = max_cheesecakes * 2
    used_oreos = max_cheesecakes * 3

    # Calculate how many boxes of graham crackers he has left over
    boxes_left_over = 14 - used_graham_crackers

    result = boxes_left_over
    return result

print(solution())