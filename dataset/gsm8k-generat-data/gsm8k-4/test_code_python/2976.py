def solution():
    """Abigail built 10 fences. Each fence took her 30 minutes to build. If she builds fences for the next 8 hours, how many fences would she have built in total?"""
    # Define the number of fences Abigail built initially
    initial_fences = 10

    # Define the time it takes to build one fence in minutes
    fence_time = 30

    # Define the available building time in minutes
    available_time = 8 * 60

    # Calculate the number of fences Abigail can build in the available time
    additional_fences = available_time // fence_time

    # Calculate the total number of fences Abigail can build
    total_fences = initial_fences + additional_fences

    # return the result
    result = total_fences
    return result

print(solution())