def solution():
    """James has 20 years of experience. 8 years ago John had twice as much experience as James. Mike started when John had 16 years of experience. What is their combined experience?"""
    # Define James' experience and calculate John's experience 8 years ago
    james_experience = 20
    john_experience_8_years_ago = (james_experience - 8) * 2

    # Calculate John's current experience and Mike's experience
    john_experience = john_experience_8_years_ago + 8
    mike_experience = john_experience - 16

    # Calculate the combined experience
    combined_experience = james_experience + john_experience + mike_experience

    # return the result
    result = combined_experience
    return result

print(solution())