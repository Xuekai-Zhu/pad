def solution():
    """Tom invites his parents and 3 siblings to his house. They each eat 3 times a day. How many plates do Tom and his guests use while they are there for the 4 days if each person uses 2 plates per meal?"""
    # Define the number of people eating at Tom's house
    num_people = 1 + 2 + 3  # Tom + parents + siblings

    # Calculate the total number of plates used per day
    plates_per_day = num_people * 3 * 2  # num_people * meals_per_day * plates_per_meal

    # Calculate the total number of plates used over the 4 days
    total_plates_used = plates_per_day * 4

    # Display the total number of plates used
    result = total_plates_used
    return result

print(solution())