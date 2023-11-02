def solution():
    first_class_seats = 10  # The small airplane has 10 seats in first class
    business_class_seats = 30  # The small airplane has 30 seats in business class
    economy_class_seats = 50  # The small airplane has 50 seats in economy class

    # Calculate the number of people in economy class
    economy_class_passengers = economy_class_seats // 2

    # Calculate the total number of people in first and business class
    first_and_business_class_passengers = economy_class_passengers

    # Add the three people in first class to the total number of people in first and business class
    first_and_business_class_passengers += 3

    # Calculate the number of unoccupied seats in business class
    unoccupied_business_class_seats = business_class_seats - first_and_business_class_passengers
    result = unoccupied_business_class_seats
    return result

print(solution())