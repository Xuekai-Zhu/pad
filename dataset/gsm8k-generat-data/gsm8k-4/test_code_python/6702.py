def solution():
    """There were 100 people in attendance at the school dance. Ten percent of the attendees were school faculty and staff. Of the remaining attendees, two-thirds were girls. How many boys attended the school dance?"""
    # Define the total number of attendees and the percentage of school faculty and staff
    total_attendees = 100
    faculty_percentage = 0.1

    # Calculate the number of school faculty and staff
    faculty_count = total_attendees * faculty_percentage

    # Calculate the number of remaining students
    remaining_attendees = total_attendees - faculty_count

    # Calculate the number of girls
    girl_count = remaining_attendees * (2/3)

    # Calculate the number of boys
    boy_count = remaining_attendees - girl_count

    # Return the result
    result = boy_count
    return result

print(solution())