def solution():
    """If it takes 8 days for 3 builders to build a cottage. How long will it take 6 builders to build the same size cottage working at the same rate?"""
    # Define the number of builders and the time it takes them to build a cottage
    num_builders = 3
    time_to_build = 8

    # Calculate the total amount of work to be done
    total_work = num_builders * time_to_build

    # Define the new number of builders
    new_num_builders = 6

    # Calculate the new time to build a cottage
    new_time_to_build = total_work / (new_num_builders)

    # return the result
    result = new_time_to_build
    return result

print(solution())