def solution():
    
    years = 25
    total_champions = years
    women_champions = int(total_champions * 0.6)
    men_champions = total_champions - women_champions
    men_with_beard = int(men_champions * 0.4)
    result = men_with_beard
    return result

print(solution())