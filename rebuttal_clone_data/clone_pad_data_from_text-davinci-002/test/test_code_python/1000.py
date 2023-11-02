def solution():
    aleesia_lost = 1.5
    alexei_lost = 2.5
    weeks_aleesia_lost = 10
    weeks_alexei_lost = 8
    total_aleesia_lost = aleesia_lost * weeks_aleesia_lost
    total_alexei_lost = alexei_lost * weeks_alexei_lost
    total_lost = total_aleesia_lost + total_alexei_lost
    result = total_lost
    return result

print(solution())