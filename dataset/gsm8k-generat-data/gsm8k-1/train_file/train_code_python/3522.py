def solution():
    """In Dana's senior high school class there were 200 students. 60% of the students were female, and 50% of the females were brunettes. If 50% of the female brunettes were under 5 feet tall, then how many female brunettes in Dana's high school senior class were under 5 feet tall?"""
    total_students = 200
    
    # Calculate number of female students
    female_students = total_students * 0.6
    
    # Calculate number of brunette females
    brunette_females = female_students * 0.5
    
    # Calculate number of female brunettes under 5 feet tall
    under_5_feet = brunette_females * (50/100)
    
    result = under_5_feet
    return result

print(solution())