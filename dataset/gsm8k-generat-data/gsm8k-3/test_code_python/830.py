def solution():
    """Forty percent of the students have elected to learn from home during the pandemic. The remaining students are divided into two equal groups, only one of which is physically in school on any day. What percent of students are present in school?"""
    # Define the percentage of students learning from home
    HOME_LEARNING_PERCENTAGE = 40

    # Calculate the percentage of students physically present in school
    in_school_percentage = (100 - HOME_LEARNING_PERCENTAGE) / 2

    # Display the percentage of students physically present in school
    result = in_school_percentage
    return result

print(solution())