def solution():
    """In preparation for the upcoming Olympics, Rita's swimming coach requires her to swim a total of 1,500 hours. Rita has already completed 50 hours of backstroke, 9 hours of breaststroke, and 121 hours of butterfly, but she is unhappy with her inconsistency. She has therefore decided to dedicate 220 hours every month practicing freestyle and sidestroke. How many months does Rita have to fulfill her coach’s requirements?"""
    # Define the number of hours Rita has already completed
    completed_hours = 50 + 9 + 121

    # Define the number of hours Rita needs to complete
    total_hours = 1500

    # Define the number of hours Rita will practice every month
    practice_hours = 220

    # Calculate the number of months Rita needs to fulfill her coach's requirements
    remaining_hours = total_hours - completed_hours
    months_needed = remaining_hours / practice_hours

    # Display the number of months needed
    result = months_needed
    return result

print(solution())