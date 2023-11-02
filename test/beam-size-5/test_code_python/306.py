def solution():
    # Calculate the total cost of business suits
    business_suit_cost = 6 * 100

    # Calculate the total cost of 3 suitcases
    suitcases_cost = 3 * 50

    # Calculate the flight ticket cost
    flight_ticket_cost = 5 * business_suit_cost + 700

    # Calculate the total cost of all business partners
    total_cost = business_suit_cost + suitcases_cost + flight_ticket_cost

    # Calculate the amount needed to save $2000
    amount_needed = 6000 - total_cost

    result = amount_needed
    return result

print(solution())