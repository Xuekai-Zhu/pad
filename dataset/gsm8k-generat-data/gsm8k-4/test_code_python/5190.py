def solution():
    """Kiaan is doing home delivery of newspapers in his neighborhood of 200 homes. After an hour of work, he has distributed newspapers to 2/5 of the homes. After another 2 hours of working, he realizes he has distributed newspapers to 60 percent of the remaining homes. How many homes does he still need to distribute the newspapers to?"""
    # Define the total number of homes
    total_homes = 200

    # Calculate the number of homes distributed to in the first hour
    homes_first_hour = total_homes * (2/5)

    # Calculate the number of homes remaining after the first hour
    homes_remaining = total_homes - homes_first_hour

    # Calculate the number of homes distributed to in the next 2 hours
    homes_next_two_hours = homes_remaining * 0.6

    # Calculate the number of homes still left to distribute newspapers to
    homes_left = total_homes - homes_first_hour - homes_next_two_hours

    # Return the result
    result = homes_left
    return result

print(solution())