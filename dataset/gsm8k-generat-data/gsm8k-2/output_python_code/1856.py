def solution():
    """Alden's family invited their relatives for a family reunion on Christmas eve. There were 50 more female adults than male adults, and children were twice the total number of adults. If there were 100 male adults, how many people attended the family reunion?"""
    male_adults = 100
    female_adults = male_adults + 50
    total_adults = male_adults + female_adults
    children = total_adults * 2
    total_people = male_adults + female_adults + children
    result = total_people
    return result

print(solution())