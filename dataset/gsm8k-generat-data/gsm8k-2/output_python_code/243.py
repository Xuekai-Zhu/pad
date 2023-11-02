def solution():
    """Mckenna starts her day at 8:00 a.m. She works in her office up to 11:00 a.m. then joins her team of developers at the conference room to talk about projects up to 13:00, from which she works for another two hours and then heads home. How many hours does Mckenna stay at work?"""
    start_time = 8
    office_time = 3
    conference_time = 2
    additional_work_time = 2
    total_work_time = office_time + conference_time + additional_work_time
    end_time = start_time + total_work_time
    result = end_time - start_time
    return result

print(solution())