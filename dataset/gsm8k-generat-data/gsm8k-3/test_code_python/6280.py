def solution():
    """Janet buys a multi-flavor pack of cheese sticks. 15 of the sticks are cheddar, 30 are mozzarella, and 45 are pepperjack. If Janet picks a cheese stick at random, what is the percentage chance it will be pepperjack?"""
    # Define the total number of cheese sticks
    total_sticks = 15 + 30 + 45

    # Calculate the percentage chance of picking a pepperjack stick
    pepperjack_chance = 45 / total_sticks * 100

    # Display the percentage chance
    result = pepperjack_chance
    return result

print(solution())