def solution():
    # Calculate the total number of slices after cutting the pizza
    total_slices = 8  # 1/2 + 1/4 + 1/8 + 1/8 = 8 slices

    # Calculate the number of slices given to Phill's friends
    friend_slices = (3 * 1) + (2 * 2)  # 3 friends get 1 slice each, 2 friends get 2 slices each

    # Calculate the number of slices left for Phill
    phill_slices = total_slices - friend_slices
    result = phill_slices
    return result

print(solution())