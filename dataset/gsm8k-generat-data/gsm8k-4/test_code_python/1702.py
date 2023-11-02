def solution():
    """Princeton had a gender reveal party and invited all of his fellow employees to celebrate with him. If the total number of guests were 60, and 2/3 were male guests, how many female guests attended the party?"""
    # Define the total number of guests and the proportion of male guests
    total_guests = 60
    male_proportion = 2/3

    # Calculate the number of male guests and female guests
    male_guests = total_guests * male_proportion
    female_guests = total_guests - male_guests

    # return the result
    result = female_guests
    return result

print(solution())