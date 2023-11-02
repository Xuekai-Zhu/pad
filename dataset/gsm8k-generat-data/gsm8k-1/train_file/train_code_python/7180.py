def solution():
    """A small airplane can seat 10 people in first class, 30 in business class, and 50 in economy class seating.
    If economy class is half full, and business class and first class have the same number of people together as economy class,
    how many seats are unoccupied in business class if only three people on the flight have first class seats?"""
    first_class_seats = 10
    business_class_seats = 30
    economy_class_seats = 50
    economy_class_occupancy = 0.5
    first_and_business_total_seats = economy_class_seats / 2
    first_and_business_occupancy = first_and_business_total_seats - 3
    business_class_occupancy = first_and_business_occupancy / 2
    unoccupied_business_class_seats = business_class_seats - business_class_occupancy
    result = unoccupied_business_class_seats
    return result

print(solution())