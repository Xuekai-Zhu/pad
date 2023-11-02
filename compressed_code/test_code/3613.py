def solution():
    
    total_passengers = 48
    women_passengers = total_passengers * 2/3
    men_passengers = total_passengers - women_passengers
    standing_men = men_passengers * 1/8
    seated_men = men_passengers - standing_men
    result = seated_men
    return result

print(solution())