def solution():
    gas_cost_per_gallon = 2  # The driver spends $2 per gallon of gas
    miles_per_gallon = 10  # The driver can drive 10 miles per gallon
    hours_driven = 10  # The driver drives for 10 hours
    driving_speed = 30  # The driver drives at a rate of 30 miles per hour
    rate_per_mile = 0.5  # The driver is paid $0.50 per mile

    # Calculate the total distance driven
    total_distance = hours_driven * driving_speed

    # Calculate the total amount spent on gas
    gas_cost = (total_distance / miles_per_gallon) * gas_cost_per_gallon

    # Calculate the total amount earned
    total_earnings = total_distance * rate_per_mile

    # Calculate the net earnings (total earnings minus gas cost)
    net_earnings = total_earnings - gas_cost
    result = net_earnings
    return result

print(solution())