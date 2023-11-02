def solution():
    """Porche has 3 hours to get all her homework done. Her math homework takes her 45 minutes. Her English homework takes her 30 minutes. Her science homework takes her 50 minutes. Her history homework takes her 25 minutes. She also has a special project due the next day. How much time does she have left to get that project done?"""
    # Define the total time Porche has to get her homework done
    total_time = 3 * 60 # Convert 3 hours to minutes

    # Calculate the time she spends on math, English, science, and history homework
    homework_time = 45 + 30 + 50 + 25

    # Calculate the time left for the special project
    project_time = total_time - homework_time

    # Convert the time back to hours and minutes
    project_hours = project_time // 60
    project_minutes = project_time % 60

    # Display the time left for the special project
    result = f"{project_hours} hours and {project_minutes} minutes"
    return result

print(solution())