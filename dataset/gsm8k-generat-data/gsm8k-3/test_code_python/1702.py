def solution():
    """
    Princeton had a gender reveal party and invited all of his fellow employees to celebrate with him.
    If the total number of guests were 60, and 2/3 were male guests, how many female guests attended the party?
    """
    # Calculate the number of male guests
    male_guests = int(60 * (2/3))

    # Calculate the number of female guests
    female_guests = 60 - male_guests

    # Display the number of female guests
    result = female_guests
    return result

print(solution())