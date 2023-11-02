def solution():
    """Milly is figuring out how long she needs to spend studying. She knows that her math homework will take 60 minutes. Her geography homework will take half as long as her math homework, and her science homework will take time equal to the mean amount of time she spent studying math and geography. How many minutes does Milly spend studying?"""
    # Define the time it takes to complete math homework
    math_time = 60

    # Define the time it takes to complete geography homework
    geo_time = math_time / 2

    # Define the mean time spent on math and geography homework
    mean_time = (math_time + geo_time) / 2

    # Define the time it takes to complete science homework
    science_time = mean_time

    # Calculate the total time Milly spends studying
    total_time = math_time + geo_time + science_time

    # Display the total time Milly spends studying
    result = total_time
    return result

print(solution())