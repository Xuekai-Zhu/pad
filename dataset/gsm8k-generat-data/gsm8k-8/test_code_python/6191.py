def solution():
    # Calculate the number of seats sold based on the 75% capacity
    seats_sold = 0.75 * 60000

    # Subtract the number of fans who stayed home
    total_attendance = seats_sold - 5000
    result = total_attendance
    return result

print(solution())