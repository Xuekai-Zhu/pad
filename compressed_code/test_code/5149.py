def solution():
    
    page_time = 30
    research_time = 45
    pages_written = 6
    editing_time = 75
    total_writing_time = pages_written * page_time
    total_time = total_writing_time + research_time + editing_time
    hours_spent = total_time / 60
    result = hours_spent
    return result

print(solution())