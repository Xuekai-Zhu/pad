def solution():
    cost_per_ride = 2
    num_rides = 0
    pass_cost = 50
    pass_duration = 30

    # Calculate the cost per ride if using a 30-day pass
    pass_per_ride_cost = pass_cost / pass_duration

    # Loop through each possible number of rides in a month
    for i in range(1, 31):
        # Calculate the total cost for taking i rides with one-way tickets
        ticket_cost = i * cost_per_ride

        # If the cost per ride with a 30-day pass is strictly cheaper than the cost per ride with one-way tickets,
        # then return the number of rides needed to make the pass cheaper
        if pass_per_ride_cost < cost_per_ride or pass_per_ride_cost <= ticket_cost / i:
            result = i
            return result

    # If no number of rides was found to make the pass cheaper, return None
    return None

print(solution())