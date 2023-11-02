def solution():
    total_passengers = 48
    women_fraction = 2/3
    men_fraction = 1 - women_fraction
    men_total = total_passengers * men_fraction
    standing_fraction = 1/8
    standing_men = men_total * standing_fraction
    seated_men = men_total - standing_men
    result = seated_men
    return result

print(solution())