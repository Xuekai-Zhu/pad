def solution():
    """Rachel is writing an essay. She writes 1 page every 30 minutes. She spends 45 minutes researching the topic. She writes a total of 6 pages. Then she spends 75 minutes editing her essay. Altogether, how many hours did she spend completing the essay?"""
    pages_written = 6
    time_per_page = 30
    research_time = 45
    editing_time = 75
    total_writing_time = pages_written * time_per_page
    total_time = total_writing_time + research_time + editing_time
    hours_spent = total_time / 60
    result = hours_spent
    return result

print(solution())