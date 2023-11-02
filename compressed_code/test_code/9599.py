def solution():
    
    champions_per_year = 1
    years = 25
    total_champions = champions_per_year * years
    women_champions = total_champions * 0.6
    men_champions = total_champions - women_champions
    men_with_beards = men_champions * 0.4
    result = men_with_beards
    return result

print(solution())