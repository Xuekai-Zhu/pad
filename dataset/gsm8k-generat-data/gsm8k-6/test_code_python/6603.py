def solution():
    # Calculate the total number of seats on the plane
    total_seats = 8 * 12

    # Calculate the number of seats that can be occupied
    occupied_seats = (3/4) * total_seats

    # Calculate the number of seats that will not be occupied
    empty_seats = total_seats - occupied_seats
    result = empty_seats
    return result

print(solution())