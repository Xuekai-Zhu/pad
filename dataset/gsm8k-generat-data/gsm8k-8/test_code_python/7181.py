def solution():
    # Calculate the number of seats in economy class that are filled
    economy_filled = 0.5 * 50

    # Calculate the total number of people in first and business class
    fb_total = economy_filled

    # Calculate the number of people in first class
    first_class = 3

    # Calculate the number of people in business class
    business_class = (fb_total - first_class) / 2

    # Calculate the number of unoccupied seats in business class
    unoccupied_seats = 30 - business_class

    result = unoccupied_seats
    return result

print(solution())