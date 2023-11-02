def solution():
    """David finished his homework in 60 minutes. He spent 15 minutes on his math homework and 18 minutes on his spelling homework. He spent the rest of the time reading for his daily reading log. How many minutes did he spend reading?"""
    total_time = 60
    math_time = 15
    spelling_time = 18
    reading_time = total_time - math_time - spelling_time
    result = reading_time
    return result

print(solution())