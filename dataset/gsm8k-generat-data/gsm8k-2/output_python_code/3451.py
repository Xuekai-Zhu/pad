def solution():
    """The American Academy of Pediatrics recommended no more than 2 hours of screen time each day for children. Mrs. Merril wants to follow a 2-hour screen time for her child. How many minutes will she allow her child to use his gadget this evening if he already used his gadget for 45 minutes in the morning?"""
    max_screen_time = 2 * 60
    used_screen_time = 45
    remaining_screen_time = max_screen_time - used_screen_time
    result = remaining_screen_time
    return result

print(solution())