def solution():
    # Calculate the ratio of slices of pizza that Buzz and the waiter will eat
    total_ratio = 5 + 8  # total ratio of slices is 5 + 8 = 13
    waiter_ratio = 8 / total_ratio  # waiter's ratio of slices is 8/13
    buzz_ratio = 5 / total_ratio  # Buzz's ratio of slices is 5/13

    # Calculate the number of slices of pizza the waiter ate
    slices_waiter = waiter_ratio * 78

    # Calculate 20 less than the number of slices of pizza the waiter ate
    result = slices_waiter - 20
    return result

print(solution())