def solution():
    
    # Define the total number of questions
    total_questions = 60

    # Calculate the number of easy questions
    easy_questions = total_questions * 0.4

    # Calculate the number of average and difficult questions
    average_difficult_questions = total_questions - easy_questions

    # Calculate the number of points Aries will get from the easy questions
    easy_points = easy_questions * 0.75

    # Calculate the number of points Aries will get from the average and difficult questions
    average_points = average_difficult_questions * 0.5

    # Calculate the total number of points Aries will get
    total_points = easy_points + average_points

    # Display the total number of points Aries will get
    result = total_points
    return result

print(solution())