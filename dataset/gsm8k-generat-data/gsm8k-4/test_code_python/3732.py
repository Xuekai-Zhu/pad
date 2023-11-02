def solution():
    """David finished his homework in 60 minutes. He spent 15 minutes on his math homework and 18 minutes on his spelling homework. He spent the rest of the time reading for his daily reading log. How many minutes did he spend reading?"""
    # Define the total time and time spent on math and spelling homework
    total_time = 60
    math_time = 15
    spelling_time = 18

    # Calculate the time spent on reading
    reading_time = total_time - math_time - spelling_time

    # Return the result
    result = reading_time
    return result

print(solution())