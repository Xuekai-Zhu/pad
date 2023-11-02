def solution():
    
    aleesia_pounds_per_week = 1.5
    aleesia_weeks = 10
    aleesia_total_pounds_lost = aleesia_pounds_per_week * aleesia_weeks

    alexei_pounds_per_week = 2.5
    alexei_weeks = 8
    alexei_total_pounds_lost = alexei_pounds_per_week * alexei_weeks

    total_pounds_lost = aleesia_total_pounds_lost + alexei_total_pounds_lost
    result = total_pounds_lost
    return result

print(solution())