def solution():
    """Porche has 3 hours to get all her homework done. Her math homework takes her 45 minutes. Her English homework takes her 30 minutes. Her science homework takes her 50 minutes. Her history homework takes her 25 minutes. She also has a special project due the next day. How much time does she have left to get that project done?"""
    
    # Define the time spent on each subject
    math_time = 45 / 60 # convert minutes to hours
    english_time = 30 / 60 # convert minutes to hours
    science_time = 50 / 60 # convert minutes to hours
    history_time = 25 / 60 # convert minutes to hours

    # Calculate the total time spent on homework
    total_homework_time = math_time + english_time + science_time + history_time

    # Calculate the time Porche has left for her special project
    project_time = 3 - total_homework_time

    # Display the time Porche has left for her special project
    result = project_time
    return result

print(solution())