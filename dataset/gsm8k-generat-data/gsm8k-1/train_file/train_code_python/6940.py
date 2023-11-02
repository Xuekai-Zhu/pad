def solution():
    """Last Sunday, Logan went to church and realized that the number of children present was 80. If there were 60 male adults, and the total number of people in the church was 200, how many female adults were present?"""
    total_people = 200
    children = 80
    male_adults = 60
    female_adults = total_people - children - male_adults
    result = female_adults
    return result

print(solution())