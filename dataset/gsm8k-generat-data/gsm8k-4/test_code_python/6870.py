def solution():
    """Jamie and Oliver are planning to go on a vacation. A plane ticket costs $24 for each person and a hotel stay costs $12 for each person per day. How much money will they spend on the vacation if they stay for 3 days?"""
    # Define the cost of a plane ticket and a hotel stay per day
    plane_ticket_cost = 24
    hotel_stay_cost = 12

    # Define the number of people going on the vacation
    num_people = 2

    # Define the duration of the vacation in days
    vacation_duration = 3

    # Calculate the total cost of plane tickets
    total_plane_cost = plane_ticket_cost * num_people

    # Calculate the total cost of hotel stay
    total_hotel_cost = hotel_stay_cost * num_people * vacation_duration

    # Calculate the total cost of the vacation
    total_cost = total_plane_cost + total_hotel_cost

    # return the result
    result = total_cost
    return result

print(solution())