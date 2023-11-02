def solution():
    """A small airplane can seat 10 people in first class, 30 in business class, and 50 in economy class seating. 
    If economy class is half full, 
    and business class and first class have the same number of people together as economy class, 
    how many seats are unoccupied in business class if only three people on the flight have first class seats?"""
    first_class_seats = 10
    business_class_seats = 30
    economy_class_seats = 50

    # Calculate the number of people in economy class
    economy_class_people = economy_class_seats * 0.5
    # Calculate the number of people in first and business class combined, based on the given information
    first_and_business_people = economy_class_people - 3
    # Divide this number by 2 to get the number of people in each of first and business class
    business_class_people = first_and_business_people / 2

    # Calculate the number of unoccupied seats in business class
    unoccupied_seats = business_class_seats - business_class_people

    result = unoccupied_seats
    return result

print(solution())