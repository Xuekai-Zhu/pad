def solution():
    num_years = 25  # The number of years we are considering
    num_champions = num_years  # Every year, there is one champion
    num_women_champions = int(num_champions * 0.6)  # 60% of champions are women
    num_men_champions = num_champions - num_women_champions  # The rest of the champions are men
    num_men_with_beards = int(num_men_champions * 0.4)  # 40% of men champions have beards
    result = num_men_with_beards
    return result

print(solution())