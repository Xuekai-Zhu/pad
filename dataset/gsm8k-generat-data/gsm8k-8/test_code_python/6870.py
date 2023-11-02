def solution():
    # Define the cost per person for a plane ticket and hotel stay per day
    plane_ticket_cost = 24
    hotel_stay_cost_per_day = 12

    # Define the number of people going on the vacation and the number of days they will stay
    num_people = 2
    num_days = 3

    # Calculate the total cost of plane tickets
    total_plane_ticket_cost = plane_ticket_cost * num_people

    # Calculate the total cost of hotel stay
    total_hotel_stay_cost = hotel_stay_cost_per_day * num_people * num_days

    # Calculate the total cost of the vacation
    total_cost = total_plane_ticket_cost + total_hotel_stay_cost
    result = total_cost
    return result

print(solution())