def solution():
    """Cindy was hired to teach 4 math courses which required her to be in the classroom for 48 hours a week altogether. How much did Cindy earn for teaching 1 math course in a month with exactly 4 weeks if her hourly rate per class is $25?"""
    # Define the number of math courses Cindy teaches
    num_courses = 4

    # Define the total number of hours Cindy works in a week
    weekly_hours = 48

    # Define the hourly rate per math class
    hourly_rate = 25

    # Calculate the total number of hours Cindy works in a month
    monthly_hours = weekly_hours * 4

    # Calculate the number of hours Cindy works per math class in a month
    class_hours = monthly_hours / num_courses

    # Calculate Cindy's earnings for teaching 1 math class in a month
    earnings = class_hours * hourly_rate

    # Display Cindy's earnings
    result = earnings
    return result

print(solution())