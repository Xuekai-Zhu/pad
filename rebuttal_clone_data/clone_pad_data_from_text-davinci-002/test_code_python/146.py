def solution():
    """Richard can clean his room in 22 minutes. Cory takes 3 minutes more than Richard to clean her room while Blake can clean his room 4 minutes more quickly than Cory. If they have to clean their rooms twice a week, how many minutes do all three spend cleaning their rooms each week?"""
    richard_time = 22
    cory_time = richard_time + 3
    blake_time = cory_time + 4
    cleaning_frequency = 2
    total_time = (richard_time + cory_time + blake_time) * cleaning_frequency
    result = total_time
    
    return result

print(solution())