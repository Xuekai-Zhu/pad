def solution():
    """Maiya has two sisters. The first sister is twice as old as Maiya. The second sister is 1 year younger than Maiya. Their average age is 5. How old is Maiya?"""
    # Define Maiya's age
    maiya_age = None

    # Find the range of possible ages for Maiya's sisters
    sister_age_range = range(1,10)

    # Iterate through the possible ages for Maiya's sisters to find Maiya's age
    for age in sister_age_range:
        # Calculate the age of Maiya's first sister
        sister1_age = age * 2
        # Calculate the age of Maiya's second sister
        sister2_age = age + 1
        # Calculate the total age of the three sisters
        total_age = sister1_age + sister2_age + age
        # Calculate the average age of the three sisters
        average_age = total_age / 3
        # Check if the average age is 5
        if average_age == 5:
            maiya_age = age

    # return Maiya's age
    result = maiya_age
    return result

print(solution())