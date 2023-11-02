def solution():
    """Last Sunday, Logan went to church and realized that the number of children present was 80. If there were 60 male adults, and the total number of people in the church was 200, how many female adults were present?"""
    # Calculate the number of children present
    children = 80

    # Calculate the number of male adults present
    male_adults = 60

    # Calculate the total number of people present
    total = 200

    # Calculate the number of female adults present
    female_adults = total - children - male_adults

    # Display the number of female adults present
    result = female_adults
    return result

print(solution())