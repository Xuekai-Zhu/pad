def solution():
    """The American Academy of Pediatrics recommended no more than 2 hours of screen time each day for children. Mrs. Merril wants to follow a 2-hour screen time for her child. How many minutes will she allow her child to use his gadget this evening if he already used his gadget for 45 minutes in the morning?"""
    # Define the maximum screen time in minutes
    MAX_SCREEN_TIME = 120

    # Subtract the time already used from the maximum screen time
    remaining_screen_time = MAX_SCREEN_TIME - 45

    # Display the remaining screen time in minutes
    result = remaining_screen_time
    return result

print(solution())