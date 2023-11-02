def solution():
    """A small airplane can seat 10 people in first class, 30 in business class, and 50 in economy class seating. If economy class is half full, and business class and first class have the same number of people together as economy class, how many seats are unoccupied in business class if only three people on the flight have first class seats?"""
    # Define the number of seats in each class
    FIRST_CLASS_SEATS = 10
    BUSINESS_CLASS_SEATS = 30
    ECONOMY_CLASS_SEATS = 50

    # Define the number of first class passengers
    first_class_passengers = 3

    # Calculate the number of economy class passengers
    economy_class_passengers = 0.5 * ECONOMY_CLASS_SEATS

    # Calculate the number of business class passengers
    business_class_passengers = economy_class_passengers - first_class_passengers

    # Calculate the number of unoccupied business class seats
    unoccupied_seats = BUSINESS_CLASS_SEATS - business_class_passengers

    # Display the number of unoccupied business class seats
    result = unoccupied_seats
    return result

print(solution())