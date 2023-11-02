def solution():
    number_of_balloons = 100
    ounces_in_a_bottle = 50
    ounces_in_a_balloon = 3
    water_needed = number_of_balloons * ounces_in_a_balloon
    bottles_needed = water_needed / ounces_in_a_bottle
    cost_per_bottle = 2.5
    total_cost = bottles_needed * cost_per_bottle
    bills_received = 2 * 10
    change_received = bills_received - total_cost
    result = change_received
    return result

print(solution())