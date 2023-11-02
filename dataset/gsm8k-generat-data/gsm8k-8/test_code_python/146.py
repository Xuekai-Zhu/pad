def solution():
    # Define the time it takes Richard to clean his room
    richard_time = 22

    # Calculate Cory's time
    cory_time = richard_time + 3

    # Calculate Blake's time
    blake_time = cory_time - 4

    # Calculate the total time spent cleaning per week for each person
    richard_total_time = richard_time * 2
    cory_total_time = cory_time * 2
    blake_total_time = blake_time * 2

    # Calculate the total time spent cleaning per week for all three
    total_time = richard_total_time + cory_total_time + blake_total_time
    result = total_time
    return result

print(solution())