def solution():
    """David finished his homework in 60 minutes. He spent 15 minutes on his math homework and 18 minutes on his spelling homework. He spent the rest of the time reading for his daily reading log. How many minutes did he spend reading?"""
    # Define the time spent on math and spelling homework
    math_time = 15
    spelling_time = 18

    # Calculate the total time spent on homework
    total_time = 60

    # Calculate the time spent reading
    reading_time = total_time - math_time - spelling_time

    # Display the time spent reading
    result = reading_time
    return result

print(solution())