def solution():
    """Eric has a chicken farm with 4 chickens. His chickens lay 3 eggs each day. If Eric collects all the eggs after 3 days, then how many eggs will Eric have collected?"""
    # Define the number of chickens and eggs laid per day
    NUM_CHICKENS = 4
    EGGS_PER_DAY = 3

    # Calculate the total number of eggs laid after 3 days
    total_eggs = NUM_CHICKENS * EGGS_PER_DAY * 3

    # return the result
    result = total_eggs
    return result

print(solution())