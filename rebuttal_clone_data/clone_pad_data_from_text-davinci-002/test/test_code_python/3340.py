def solution():
    total_community_members = 2000
    adult_men = total_community_members * 0.3
    adult_women = adult_men * 2
    children = total_community_members - (adult_men + adult_women)
    result = children
    return result

print(solution())