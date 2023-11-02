def solution():
    """Every day, while going to school, Shane drives a total of 10 miles. Calculate the total distance he drives in an 80 day semester from home to school and back."""
    # Calculate the distance Shane drives in one day
    daily_distance = 10 * 2  # to and from school

    # Calculate the total distance Shane drives in an 80 day semester
    semester_distance = daily_distance * 80

    # Display the total distance Shane drives
    result = semester_distance
    return result

print(solution())