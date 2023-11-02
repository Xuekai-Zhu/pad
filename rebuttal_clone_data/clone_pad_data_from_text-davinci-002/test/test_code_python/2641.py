def solution():
    total_passengers = 48
    fraction_women = 2/3
    women_on_bus = total_passengers * fraction_women
    men_on_bus = total_passengers - women_on_bus
    fraction_men_standing = 1/8
    men_standing = men_on_bus * fraction_men_standing
    men_seated = men_on_bus - men_standing
    result = men_seated
    
    return result

print(solution())