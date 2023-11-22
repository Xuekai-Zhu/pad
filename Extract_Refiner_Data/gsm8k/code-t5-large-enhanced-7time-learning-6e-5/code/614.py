def solution():
    
    # Define the number of rows and seats per row
    rows = 4
    seats_per_row = 18

    # Calculate the total number of seats
    total_seats = rows * seats_per_row

    # Calculate the number of seats occupied by administrators
    admin_seats = total_seats // 4

    # Calculate the number of remaining seats
    remaining_seats = total_seats - admin_seats

    # Calculate the number of seats occupied by parents
    parent_seats = remaining_seats // 3

    # Calculate the number of seats occupied by students
    student_seats = remaining_seats - parent_seats

    # Display the number of students
    result = student_seats
    return result

print(solution())