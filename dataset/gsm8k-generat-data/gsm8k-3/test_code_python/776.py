def solution():
    """Amber worked for 12 hours last weekend. Armand worked one-third as long and Ella worked twice as long. How many hours did the 3 people work in total?"""
    # Define the number of hours worked by Amber, Armand, and Ella
    amber_hours = 12
    armand_hours = amber_hours / 3
    ella_hours = amber_hours * 2

    # Calculate the total number of hours worked
    total_hours = amber_hours + armand_hours + ella_hours

    # Display the total number of hours worked
    result = total_hours
    return result

print(solution())