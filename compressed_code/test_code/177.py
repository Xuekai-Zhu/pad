def solution():
    
    start_time = 8
    office_time = 3
    conference_time = 2
    additional_work_time = 2
    total_work_time = office_time + conference_time + additional_work_time
    end_time = start_time + total_work_time
    result = end_time - start_time
    return result

print(solution())