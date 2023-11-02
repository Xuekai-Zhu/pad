def solution():
    """In preparation for the upcoming Olympics, Rita's swimming coach requires her to swim a total of 1,500 hours. Rita has already completed 50 hours of backstroke, 9 hours of breaststroke, and 121 hours of butterfly,
    but she is unhappy with her inconsistency. She has therefore decided to dedicate 220 hours every month practicing freestyle and sidestroke. How many months does Rita have to fulfill her coach’s requirements?"""
    total_hours_required = 1500
    hours_completed = 50 + 9 + 121
    hours_to_practice_per_month = 220
    hours_left_to_complete = total_hours_required - hours_completed
    months_required = hours_left_to_complete / hours_to_practice_per_month
    result = months_required
    return result

print(solution())