def solution():
    total_students = 100  # assume there are 100 students in total
    girl_percentage = 40
    boy_percentage = 100 - girl_percentage

    # Calculate the number of girls and boys in the lunchroom
    num_girls = (girl_percentage/100) * total_students
    num_boys = (boy_percentage/100) * total_students

    # Calculate the total number of students in the lunchroom
    total_students = num_girls + num_boys

    # Calculate the number of monitors needed in the lunchroom
    num_monitors_needed = round(total_students / 15)

    # Check if the number of monitors needed matches the number of monitors available
    if num_monitors_needed != 8:
        return "Error: Incorrect number of monitors available."

    # Calculate the total number of cartons of milk consumed by boys and girls
    total_milk_consumed = (num_girls * 2) + (num_boys * 1)

    result = total_milk_consumed
    return result

print(solution())