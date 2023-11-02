def solution():
    """There are 34 kids signed up to compete in the talent show. There are 22 more girls than boys signed up to compete. How many girls are signed up to compete in the talent show?"""
    # Define the total number of kids signed up
    total_kids = 34

    # Define the difference in numbers between girls and boys
    gender_diff = 22

    # Calculate the number of boys signed up
    boys = (total_kids - gender_diff) / 2

    # Calculate the number of girls signed up
    girls = boys + gender_diff

    # Return the number of girls signed up
    result = girls
    return result

print(solution())