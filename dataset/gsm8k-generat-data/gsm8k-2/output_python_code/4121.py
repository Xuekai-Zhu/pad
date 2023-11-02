def solution():
    """Alex has 960 plant pictures and wants to find out how many of each plant she has pictures of. It will take a program 2 minutes to process each picture. How many hours will it take to process all of the pictures?"""
    total_pictures = 960
    process_time_per_picture = 2 # in minutes
    total_process_time = total_pictures * process_time_per_picture # in minutes
    total_process_time_hours = total_process_time / 60 # in hours
    result = total_process_time_hours
    return result

print(solution())