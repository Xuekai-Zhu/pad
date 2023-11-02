def solution():
    """In the last 25 years, 60% of Scrabble champions have been women and the rest have been men. There is one champion per year. Of the men, 40% had a beard. How many men with beards have been Scrabble champion?"""
    years = 25
    total_champions = years
    women_champions = int(total_champions * 0.6)
    men_champions = total_champions - women_champions
    men_with_beard = int(men_champions * 0.4)
    result = men_with_beard
    return result

print(solution())