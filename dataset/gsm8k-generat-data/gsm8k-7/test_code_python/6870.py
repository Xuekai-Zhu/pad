def solution():
    num_people = 2
    plane_ticket_cost = 24
    hotel_cost_per_day = 12
    num_days = 3

    # Calculate the total cost of plane tickets
    plane_ticket_total = plane_ticket_cost * num_people

    # Calculate the total cost of hotel stay
    hotel_total = hotel_cost_per_day * num_people * num_days

    # Calculate the total cost of the vacation
    total_cost = plane_ticket_total + hotel_total
    result = total_cost
    return result

print(solution())