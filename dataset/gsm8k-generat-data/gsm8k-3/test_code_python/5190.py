def solution():
    """Kiaan is doing home delivery of newspapers in his neighborhood of 200 homes. After an hour of work, he has distributed newspapers to 2/5 of the homes. After another 2 hours of working, he realizes he has distributed newspapers to 60 percent of the remaining homes. How many homes does he still need to distribute the newspapers to?"""
    # Define the total number of homes
    total_homes = 200

    # Calculate the number of homes distributed in the first hour
    homes_distributed_1 = int(2/5 * total_homes)

    # Calculate the number of homes remaining after the first hour
    homes_remaining_1 = total_homes - homes_distributed_1

    # Calculate the number of homes distributed in the next 2 hours
    homes_distributed_2 = int(0.6 * homes_remaining_1)

    # Calculate the total number of homes distributed
    total_homes_distributed = homes_distributed_1 + homes_distributed_2

    # Calculate the number of homes still needing newspapers
    homes_remaining_2 = total_homes - total_homes_distributed

    # Display the number of homes still needing newspapers
    result = homes_remaining_2
    return result

print(solution())