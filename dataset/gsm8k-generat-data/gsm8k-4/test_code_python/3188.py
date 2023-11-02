def solution():
    """Tom invites his parents and 3 siblings to his house. They each eat 3 times a day. How many plates do Tom and his guests use while they are there for the 4 days if each person uses 2 plates per meal?"""
    # Define the number of guests
    num_guests = 5

    # Define the number of meals per day
    meals_per_day = 3

    # Define the number of plates used per meal
    plates_per_meal = 2

    # Define the number of days
    num_days = 4

    # Calculate the total number of plates used
    total_plates = num_guests * meals_per_day * plates_per_meal * num_days

    # Return the result
    result = total_plates
    return result

print(solution())