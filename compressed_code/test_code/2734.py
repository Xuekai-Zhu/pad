def solution():
    
    total_students = 200
    female_percent = 0.6
    brunette_female_percent = 0.5
    brunette_female_under_5_percent = 0.5
    females = total_students * female_percent
    brunette_females = females * brunette_female_percent
    brunette_females_under_5 = brunette_females * brunette_female_under_5_percent
    result = brunette_females_under_5
    return result

print(solution())