def solution():
    """Eric has a chicken farm with 4 chickens. His chickens lay 3 eggs each day. If Eric collects all the eggs after 3 days, then how many eggs will Eric have collected?"""
    # Define the number of chickens and eggs produced per day
    NUM_CHICKENS = 4
    EGGS_PER_CHICKEN_PER_DAY = 3

    # Calculate the total number of eggs produced in 3 days
    total_eggs = NUM_CHICKENS * EGGS_PER_CHICKEN_PER_DAY * 3

    # Display the total number of eggs collected
    result = total_eggs
    return result

print(solution())