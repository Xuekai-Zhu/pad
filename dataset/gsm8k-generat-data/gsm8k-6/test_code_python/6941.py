def solution():
    # Calculate the number of female adults present
    total_adults = 200 - 80  # number of adults = total - children
    male_adults = 60  # given that there were 60 male adults
    female_adults = total_adults - male_adults
    result = female_adults
    return result

print(solution())