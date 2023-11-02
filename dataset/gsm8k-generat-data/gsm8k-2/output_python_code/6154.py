def solution():
    """A pickup truck can fill 20 eight gallon water cans (each can filled three quarters of its capacity) in three hours. If each can is filled to full capacity instead, how long, in hours, will it take to fill 25 cans?"""
    capacity = 8 * 0.75
    filled_capacity = 8
    cans_per_hour = 20 / 3
    cans_to_fill = 25
    time_to_fill_partial = cans_to_fill * capacity / cans_per_hour
    time_to_fill_full = cans_to_fill * filled_capacity / cans_per_hour
    result = time_to_fill_full
    return result

print(solution())