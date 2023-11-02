def solution():
    num_rides = 9
    ticket_price = 2
    num_tickets_per_ride = 2
    bracelet_cost = 30

    # Calculate the total cost of all rides of tickets
    total_tickets_cost = num_rides * ticket_price

    # Calculate the total cost of all rides of bracelet
    total_bracelet_cost = num_rides * bracelet_cost

    # Calculate how much money David saves
    savings = total_tickets_cost - total_bracelet_cost
    result = savings
    return result

print(solution())