def solution():
    """Rachel is writing an essay. She writes 1 page every 30 minutes. She spends 45 minutes researching the topic. She writes a total of 6 pages. Then she spends 75 minutes editing her essay. Altogether, how many hours did she spend completing the essay?"""
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