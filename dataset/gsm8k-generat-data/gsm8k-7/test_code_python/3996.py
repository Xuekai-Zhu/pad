def solution():
    pizza_slices = 78
    waiter_ratio = 8 / 13  # Ratio of waiter slices to total slices
    waiter_slices = pizza_slices * waiter_ratio
    buzz_slices = pizza_slices - waiter_slices
    buzz_share = buzz_slices / 5  # Buzz's share based on his ratio
    waiter_share = waiter_slices / 8  # Waiter's share based on his ratio
    num_slices_not_eaten = 20 - waiter_share
    result = num_slices_not_eaten
    return result

print(solution())