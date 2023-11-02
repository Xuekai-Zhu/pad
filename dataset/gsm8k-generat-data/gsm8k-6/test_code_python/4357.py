def solution():
    # Calculate the total number of seats in the cafeteria
    total_seats = 15 * 10  # 15 tables, each seating 10 people

    # Calculate the number of seats usually taken
    seats_taken = int(total_seats * (9/10)) # 1/10 of the seats are usually left unseated

    result = seats_taken
    return result

print(solution())