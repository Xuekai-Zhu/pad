def solution():
    """Meso can type 15 pages in 5 minutes. Tyler can type the same 15 pages in 3 minutes.  How many minutes would it take Meso and Tyler to type 40 pages working together?"""
    # Define the typing speed for each person in pages per minute
    meso_speed = 15 / 5
    tyler_speed = 15 / 3

    # Calculate the time it would take for Meso and Tyler to complete 40 pages together
    total_speed = meso_speed + tyler_speed
    total_time = 40 / total_speed

    # Return the result in minutes
    result = total_time
    return result

print(solution())