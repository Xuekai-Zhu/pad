def solution():
    # Calculate the total number of seats in the airplane
    total_seats = 10 + 30 + 50

    # Calculate the number of people in economy class
    economy_class_people = 0.5 * 50

    # Calculate the number of people in business and first class combined
    bf_class_people = economy_class_people

    # Subtract the number of people in first class from the total number of seats
    total_seats -= 3

    # Subtract the number of people in business and first class combined from the total number of seats
    total_seats -= bf_class_people

    # Calculate the number of unoccupied seats in business class
    unoccupied_seats = 30 - bf_class_people

    result = unoccupied_seats
    return result

print(solution())