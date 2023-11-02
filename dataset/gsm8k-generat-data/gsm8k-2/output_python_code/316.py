def solution():
    """Madeline spends 18 hours a week in class. She spends 4 hours per day working on homework. She spends 8 hours per day sleeping. She works part-time 20 hours per week. How many hours left over does Madeline have?"""
    class_hours = 18
    homework_hours = 4 * 7
    sleep_hours = 8 * 7
    job_hours = 20
    total_hours = class_hours + homework_hours + sleep_hours + job_hours
    remaining_hours = 7 * 24 - total_hours
    result = remaining_hours
    return result

print(solution())