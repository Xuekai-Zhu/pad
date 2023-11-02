def solution():
    """Sam spends sixty minutes studying Science, eighty minutes in Math, and forty minutes in Literature. How many hours does Sam spend studying the three subjects?"""
    # Define the time spent in each subject in minutes
    science_time = 60
    math_time = 80
    literature_time = 40

    # Calculate the total time spent studying in minutes
    total_time_minutes = science_time + math_time + literature_time

    # Convert the total time to hours
    total_time_hours = total_time_minutes / 60

    # Return the result
    result = total_time_hours
    return result

print(solution())