def solution():
    """James has 20 years of experience.  8 years ago John had twice as much experience as James.  Mike started when John had 16 years of experience.  What is their combined experience?"""
    # Define James' experience
    james_exp = 20

    # Define the number of years ago when John had twice as much experience as James
    john_twice_exp_years_ago = 8

    # Calculate James' experience at that time
    james_exp_years_ago = james_exp - john_twice_exp_years_ago

    # Calculate John's experience at that time
    john_exp_years_ago = 2 * james_exp_years_ago

    # Calculate John's current experience
    john_exp = john_exp_years_ago + john_twice_exp_years_ago

    # Calculate Mike's experience
    mike_exp = john_exp - 16

    # Calculate the total combined experience
    total_exp = james_exp + john_exp + mike_exp

    # Display the total combined experience
    result = total_exp
    return result

print(solution())