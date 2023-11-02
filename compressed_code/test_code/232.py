def solution():
    
    class_hours = 18
    homework_hours = 4 * 7
    sleep_hours = 8 * 7
    job_hours = 20
    total_hours = class_hours + homework_hours + sleep_hours + job_hours
    remaining_hours = 7 * 24 - total_hours
    result = remaining_hours
    return result

print(solution())