def solution():
    """Megan is making food for a party.  She has to spend 20 minutes preparing one dish in the oven.  Each dish can feed 5 people.  She spends 2 hours preparing as many of these dishes as she can for the party.  How many people can she feed with these dishes?"""
    # Define the time it takes to prepare one dish and the number of people each dish can feed
    TIME_PER_DISH = 20 # in minutes
    PEOPLE_PER_DISH = 5

    # Convert the total preparation time to minutes
    total_time = 2 * 60 # in minutes

    # Calculate the maximum number of dishes Megan can prepare in the total time
    max_dishes = total_time // TIME_PER_DISH

    # Calculate the maximum number of people Megan can feed with the dishes
    max_people = max_dishes * PEOPLE_PER_DISH

    # Display the maximum number of people Megan can feed
    result = max_people
    return result

print(solution())