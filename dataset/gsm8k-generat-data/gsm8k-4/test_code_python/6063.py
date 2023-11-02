def solution():
    """Megan is making food for a party. She has to spend 20 minutes preparing one dish in the oven. Each dish can feed 5 people. She spends 2 hours preparing as many of these dishes as she can for the party. How many people can she feed with these dishes?"""
    # Define the time Megan has to prepare dishes (in minutes)
    time_in_minutes = 2 * 60

    # Define the time it takes to prepare one dish (in minutes)
    dish_time_in_minutes = 20

    # Calculate the number of dishes Megan can prepare
    num_dishes = time_in_minutes // dish_time_in_minutes

    # Calculate the number of people Megan can feed
    num_people = num_dishes * 5

    # return the result
    result = num_people
    return result

print(solution())