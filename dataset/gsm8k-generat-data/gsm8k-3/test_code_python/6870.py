def solution():
    """Jamie and Oliver are planning to go on a vacation. A plane ticket costs $24 for each person and a hotel stay costs $12 for each person per day. How much money will they spend on the vacation if they stay for 3 days?"""
    # Define the cost of a plane ticket and a hotel stay per person per day
    PLANE_TICKET_PRICE = 24
    HOTEL_COST_PER_DAY = 12

    # Define the number of people going on the vacation
    num_people = 2

    # Define the duration of the vacation in days
    num_days = 3

    # Calculate the total cost of the plane tickets
    plane_tickets_cost = num_people * PLANE_TICKET_PRICE

    # Calculate the total cost of the hotel stay
    hotel_stay_cost = num_people * HOTEL_COST_PER_DAY * num_days

    # Calculate the total cost of the vacation
    total_cost = plane_tickets_cost + hotel_stay_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())