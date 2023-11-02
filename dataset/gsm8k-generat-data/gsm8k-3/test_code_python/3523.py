def solution():
    """In Dana's senior high school class there were 200 students.  60% of the students were female, and 50% of the females were brunettes.  If 50% of the female brunettes were under 5 feet tall, then how many female brunettes in Dana's high school senior class were under 5 feet tall?"""
    # Define the total number of students and the percentage of females and female brunettes
    total_students = 200
    female_percentage = 0.6
    brunette_percentage = 0.5
    under_5_percentage = 0.5

    # Calculate the number of females and female brunettes
    female_count = total_students * female_percentage
    brunette_count = female_count * brunette_percentage

    # Calculate the number of female brunettes under 5 feet tall
    under_5_count = brunette_count * under_5_percentage

    # Round the answer to the nearest whole number
    under_5_count = round(under_5_count)

    # Display the number of female brunettes under 5 feet tall
    result = under_5_count
    return result

print(solution())