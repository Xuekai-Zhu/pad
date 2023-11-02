def solution():
    first_class_capacity = 10
    business_class_capacity = 30
    economy_class_capacity = 50

    num_first_class_passengers = 3

    # Calculate the number of passengers in economy class
    num_economy_class_passengers = economy_class_capacity // 2

    # Calculate the total number of passengers in business and first class combined
    num_business_and_first_class_passengers = num_economy_class_passengers

    # Subtract the number of first class passengers from the total number of business and first class passengers
    num_business_class_passengers = num_business_and_first_class_passengers - num_first_class_passengers

    # Calculate the number of unoccupied seats in business class
    num_unoccupied_business_class_seats = business_class_capacity - num_business_class_passengers

    result = num_unoccupied_business_class_seats
    return result

print(solution())