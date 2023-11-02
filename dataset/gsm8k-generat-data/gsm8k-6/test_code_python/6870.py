def solution():
    # Calculate the total cost of the vacation for both Jamie and Oliver
    plane_ticket_cost = 24 * 2  # two people are going so the cost is doubled
    hotel_stay_cost = 12 * 2 * 3  # two people staying for 3 days, so cost is doubled and multiplied by 3
    total_cost = plane_ticket_cost + hotel_stay_cost
    result = total_cost
    return result

print(solution())