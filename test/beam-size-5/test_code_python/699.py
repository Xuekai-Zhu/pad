def solution():
    
    total_males = 8
    total_females = 6
    male_dumplings = 3
    female_dumplings = 3
    total_dumplings = (total_males * male_dumplings) + (total_females * female_dumplings)
    larry_dumplings = (total_males * male_dumplings) + (total_females * female_dumplings)
    result = larry_dumplings
    return result

print(solution())