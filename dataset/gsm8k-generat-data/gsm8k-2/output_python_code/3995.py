def solution():
    """If Buzz bought a pizza with 78 slices at a restaurant and then decided to share it with the waiter in the ratio of 5:8, with Buzz's ratio being 5, what's twenty less the number of slices of pizza that the waiter ate?"""
    total_slices = 78
    buzz_ratio = 5
    waiter_ratio = 8
    total_ratio = buzz_ratio + waiter_ratio
    waiter_slices = (waiter_ratio/total_ratio) * total_slices
    buzz_slices = total_slices - waiter_slices
    result = 20 - waiter_slices
    return result

print(solution())