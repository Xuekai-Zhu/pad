def solution():
    num_people = 2
    ticket_price = 5.0
    bus_fare_per_person = 1.5
    num_bus_trips = 2

    total_tickets_cost = num_people * ticket_price
    total_bus_cost = num_people * bus_fare_per_person * num_bus_trips

    total_spent = total_tickets_cost + total_bus_cost
    money_left = 40 - total_spent
    result = money_left
    return result

print(solution())