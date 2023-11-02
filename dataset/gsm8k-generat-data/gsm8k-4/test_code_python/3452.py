def solution():
    """The American Academy of Pediatrics recommended no more than 2 hours of screen time each day for children. Mrs. Merril wants to follow a 2-hour screen time for her child. How many minutes will she allow her child to use his gadget this evening if he already used his gadget for 45 minutes in the morning?"""
    # Define the maximum screen time allowed in a day
    MAX_SCREEN_TIME = 2 * 60  # 2 hours in minutes

    # Calculate the remaining screen time for the child
    remaining_screen_time = MAX_SCREEN_TIME - 45

    # Display the result in minutes
    result = remaining_screen_time
    return result

print(solution())