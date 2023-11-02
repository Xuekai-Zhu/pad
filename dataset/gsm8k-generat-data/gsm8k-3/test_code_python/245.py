def solution():
    """Mckenna starts her day at 8:00 a.m. She works in her office up to 11:00 a.m. then joins her team of developers at the conference room to talk about projects up to 13:00, from which she works for another two hours and then heads home. How many hours does Mckenna stay at work?"""
    # Define the start and end times of each segment of work
    office_start = 8
    office_end = 11
    conference_start = 11
    conference_end = 13
    afternoon_start = 13
    afternoon_end = 15

    # Calculate the total hours worked
    total_hours = (office_end - office_start) + (conference_end - conference_start) + (afternoon_end - afternoon_start)

    # Display the total hours worked
    result = total_hours
    return result

print(solution())