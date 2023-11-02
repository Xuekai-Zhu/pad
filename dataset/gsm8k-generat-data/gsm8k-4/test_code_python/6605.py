def solution():
    """In preparation for the upcoming Olympics, Rita's swimming coach requires her to swim a total of 1,500 hours. Rita has already completed 50 hours of backstroke, 9 hours of breaststroke, and 121 hours of butterfly, but she is unhappy with her inconsistency. She has therefore decided to dedicate 220 hours every month practicing freestyle and sidestroke. How many months does Rita have to fulfill her coach’s requirements?"""
    # Define the total number of hours Rita has already completed
    total_hours_completed = 50 + 9 + 121

    # Define the total number of hours Rita still needs to complete
    hours_remaining = 1500 - total_hours_completed

    # Calculate the number of months Rita needs to fulfill her coach's requirements
    months_needed = hours_remaining / 220

    # Round up to the nearest integer
    months_needed = math.ceil(months_needed)

    # return the result
    result = months_needed
    return result

print(solution())