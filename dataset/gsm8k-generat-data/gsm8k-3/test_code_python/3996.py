def solution():
    """If Buzz bought a pizza with 78 slices at a restaurant and then decided to share it with the waiter in the ratio of 5:8, with Buzz's ratio being 5, what's twenty less the number of slices of pizza that the waiter ate?"""
    # Calculate the total slices Buzz and the waiter will get
    total_slices = 5 + 8
    # Calculate the number of slices Buzz will get
    buzz_slices = (5/total_slices) * 78
    # Calculate the number of slices the waiter will get
    waiter_slices = (8/total_slices) * 78
    # Calculate 20 less than the number of slices the waiter ate
    result = int(waiter_slices - 20)
    return result

print(solution())