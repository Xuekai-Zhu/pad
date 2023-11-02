def solution():
    
    total_members = 2000
    adult_men_percentage = 0.3
    adult_men = total_members * adult_men_percentage
    adult_women = adult_men * 2
    children = total_members - adult_men - adult_women
    result = children
    return result

print(solution())