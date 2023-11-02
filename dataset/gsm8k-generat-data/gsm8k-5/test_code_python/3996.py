def solution():
    total_slices = 78  # The pizza has 78 slices
    buzz_ratio = 5  # Buzz's ratio is 5
    waiter_ratio = 8  # Waiter's ratio is 8
    total_ratio = buzz_ratio + waiter_ratio  # Total ratio is 5+8=13

    # Calculate the number of slices Buzz will keep
    buzz_slices = (buzz_ratio/total_ratio) * total_slices

    # Calculate the number of slices the waiter will eat
    waiter_slices = (waiter_ratio/total_ratio) * total_slices

    # Calculate 20 less than the number of slices the waiter ate
    result = waiter_slices - 20
    return result

print(solution())