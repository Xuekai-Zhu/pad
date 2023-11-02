def solution():
    """Alex is working on a science project and has taken pictures of all of the plants in a park near her home. She wants to find out how many of each plant she has pictures of, but she has 960 pictures, and counting them all will take her a long time. Her teacher suggested she use a program on the computer that can automatically tell her what plant is in each picture and count them for her. It will take the program 2 minutes to process each picture. How many hours will it take to process all of the pictures?"""
    total_pictures = 960
    time_per_picture = 2 # in minutes
    time_per_hour = 60 # in minutes
    total_time = (total_pictures * time_per_picture) / time_per_hour
    result = total_time
    return result

print(solution())