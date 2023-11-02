def solution():
    """Harry is 50 years old. His father is currently 24 years older than he is. How old was his mother when she gave birth to him if she is younger than his father by 1/25 of Harry's current age?"""
    # Define Harry's age and the age difference between him and his father
    HARRY_AGE = 50
    FATHER_AGE_DIFF = 24

    # Calculate Harry's father's age
    father_age = HARRY_AGE + FATHER_AGE_DIFF

    # Calculate the age difference between Harry's mother and father
    mother_father_age_diff = HARRY_AGE / 25

    # Calculate Harry's mother's age when she gave birth to him
    mother_age = father_age - mother_father_age_diff

    # Display Harry's mother's age
    result = mother_age
    return result

print(solution())