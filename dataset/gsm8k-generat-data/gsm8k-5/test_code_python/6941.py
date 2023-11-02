def solution():
    # Calculate the number of female adults by subtracting the number of children and male adults from the total number of people
    total_people = 200
    children = 80
    male_adults = 60
    female_adults = total_people - children - male_adults
    result = female_adults
    return result

print(solution())