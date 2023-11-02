def solution():
    """In Dana's senior high school class there were 200 students. 60% of the students were female, and 50% of the females were brunettes. If 50% of the female brunettes were under 5 feet tall, then how many female brunettes in Dana's high school senior class were under 5 feet tall?"""
    # Define the total number of students
    total_students = 200

    # Calculate the number of female students
    female_students = total_students * 0.6

    # Calculate the number of brunette female students
    brunette_females = female_students * 0.5

    # Calculate the number of under 5 feet tall brunette females
    under_5_feet_brunettes = brunette_females * 0.5

    # return the result
    result = under_5_feet_brunettes
    return result

print(solution())