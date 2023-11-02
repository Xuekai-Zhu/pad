def solution():
    """Last Sunday, Logan went to church and realized that the number of children present was 80. If there were 60 male adults, and the total number of people in the church was 200, how many female adults were present?"""
    # Define the number of children and male adults
    children = 80
    male_adults = 60

    # Calculate the number of female adults
    total = 200
    female_adults = total - children - male_adults

    # return the result
    result = female_adults
    return result

print(solution())