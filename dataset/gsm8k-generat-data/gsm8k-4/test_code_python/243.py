def solution():
    """Mckenna starts her day at 8:00 a.m. She works in her office up to 11:00 a.m. then joins her team of developers at the conference room to talk about projects up to 13:00, from which she works for another two hours and then heads home. How many hours does Mckenna stay at work?"""
    # Define the start and end times of Mckenna's work day
    start_time = 8
    end_time = 18

    # Calculate the amount of time Mckenna spends in the office before the meeting
    office_time = 11 - start_time

    # Calculate the amount of time Mckenna spends in the meeting
    meeting_time = 13 - 11

    # Calculate the amount of time Mckenna spends working after the meeting
    work_time = 2

    # Calculate the total time Mckenna spends at work
    total_time = office_time + meeting_time + work_time

    result = total_time
    return result

print(solution())