def solution():
    """Vivian is responsible for making sure her students get 2 15-minute recess breaks a day, a 30-minute lunch and another 20-minute recess break. How much time do her students spend outside of class?"""
    # Define the length of each break in minutes
    recess_break = 15
    lunch_break = 30
    extra_recess_break = 20

    # Define the number of breaks per day
    num_recess_breaks = 2

    # Calculate the total time spent outside of class
    total_time = (recess_break * num_recess_breaks) + lunch_break + extra_recess_break

    # Return the result in hours and minutes
    hours = total_time // 60
    minutes = total_time % 60
    result = f"{hours} hours and {minutes} minutes"
    return result

print(solution())