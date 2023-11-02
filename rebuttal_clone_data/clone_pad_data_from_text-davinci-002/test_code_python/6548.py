def solution():
    cost_of_zoo_entry = 5
    cost_of_bus_fare = 1.50
    money_available = 40
    number_of_people = 2
    total_cost_of_zoo_entry = cost_of_zoo_entry * number_of_people
    total_cost_of_bus_fare = cost_of_bus_fare * number_of_people
    total_cost = total_cost_of_zoo_entry + total_cost_of_bus_fare
    money_left = money_available - total_cost
    result = money_left
    return result

print(solution())