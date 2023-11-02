def solution():
    """In a glee club, there are two times as many female than male members. How many female members are there if there are 18 members in the club?"""
    # Define the total number of members and the ratio of females to males
    total_members = 18
    female_to_male_ratio = 2

    # Calculate the total number of males
    num_males = total_members / (female_to_male_ratio + 1)

    # Calculate the total number of females
    num_females = female_to_male_ratio * num_males

    result = num_females
    return result

print(solution())