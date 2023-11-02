def solution():
    """Alex is working on a science project and has taken pictures of all of the plants in a park near her home. She wants to find out how many of each plant she has pictures of, but she has 960 pictures, and counting them all will take her a long time. Her teacher suggested she use a program on the computer that can automatically tell her what plant is in each picture and count them for her. It will take the program 2 minutes to process each picture. How many hours will it take to process all of the pictures?"""
    # Define the number of pictures and processing time per picture
    NUM_PICTURES = 960
    PROCESSING_TIME = 2 # in minutes

    # Calculate the total processing time in minutes
    total_processing_time = NUM_PICTURES * PROCESSING_TIME

    # Convert the total processing time to hours
    hours = total_processing_time / 60

    # Display the total processing time in hours
    result = hours
    return result

print(solution())