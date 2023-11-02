def solution():
    """Harry is 50 years old. His father is currently 24 years older than he is. How old was his mother when she gave birth to him if she is younger than his father by 1/25 of Harry's current age?"""
    # Define Harry's age and his father's age
    harry_age = 50
    father_age = harry_age + 24

    # Calculate the age difference between Harry's mother and father
    age_difference = (1/25) * harry_age

    # Calculate the mother's age when Harry was born
    mother_age = (father_age - age_difference) - (harry_age - age_difference)

    # Return the result
    result = mother_age
    return result

print(solution())