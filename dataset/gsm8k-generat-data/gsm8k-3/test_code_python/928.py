def solution():
    """In a glee club, there are two times as many female than male members. How many female members are there if there are 18 members in the club?"""
    # Define the number of male members
    males = x

    # Calculate the number of female members
    females = 2 * males

    # Calculate the total number of members
    total = males + females

    # Solve for the number of males given that the total number of members is 18
    males = 18 / 3  # We note that x + 2x = 3x, so x = (1/3)*18 = 6

    # Calculate the number of female members
    females = 2 * males

    result = females
    return result

print(solution())