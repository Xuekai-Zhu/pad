def solution():
    """A small airplane can seat 10 people in first class, 30 in business class, and 50 in economy class seating. If economy class is half full, and business class and first class have the same number of people together as economy class, how many seats are unoccupied in business class if only three people on the flight have first class seats?"""
    # Define the capacities of each class
    first_class_capacity = 10
    business_class_capacity = 30
    economy_class_capacity = 50

    # Calculate the number of economy class seats occupied
    economy_class_occupied = economy_class_capacity // 2

    # Calculate the number of first and business class seats occupied, given that they have the same number of people together as economy class
    first_class_and_business_class_occupied = economy_class_occupied

    # Subtract the number of first class seats occupied (which is given to be 3) to get the number of business class seats occupied
    business_class_occupied = first_class_and_business_class_occupied - 3

    # Calculate the number of unoccupied business class seats
    business_class_unoccupied = business_class_capacity - business_class_occupied

    # return the result
    result = business_class_unoccupied
    return result

print(solution())