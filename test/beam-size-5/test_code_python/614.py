def solution():
    
    # Define the number of rows and seats per row
    rows = 4
    seats_per_row = 18

    # Calculate the total number of seats
    total_seats = rows * seats_per_row

    # Calculate the number of occupied seats
    occupied_seats = total_seats // 4

    # Calculate the number of remaining seats
    remaining_seats = total_seats - occupied_seats

    # Calculate the number of occupied seats
    occupied_seats = remaining_seats // 3

    # Calculate the number of students
    students = remaining_seats - occupied_seats

    # Display the number of students
    result = students
    return result

print(solution())