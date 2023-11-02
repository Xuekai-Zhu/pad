def solution():
    """Janice needs to go to watch a movie in 2 hours. before she could leave, she needs to finish her homework which takes 30 minutes; clean her room which takes half as long as her homework; walk the dog which takes 5 minutes more than making homework; take out the trash which takes 1/6 of the time it takes her to do the homework. How many more minutes do Janice have left before the movie starts?"""
    # Define the time it takes for Janice to do her homework
    homework_time = 30

    # Calculate the time it takes for Janice to clean her room
    room_cleaning_time = homework_time / 2

    # Calculate the time it takes for Janice to walk the dog
    dog_walking_time = homework_time + 5

    # Calculate the time it takes for Janice to take out the trash
    trash_taking_time = homework_time / 6

    # Calculate the total time Janice needs to finish her tasks
    total_time = homework_time + room_cleaning_time + dog_walking_time + trash_taking_time

    # Calculate the time left before the movie starts
    time_left = (2*60) - total_time

    # Display the time left
    result = time_left
    return result

print(solution())