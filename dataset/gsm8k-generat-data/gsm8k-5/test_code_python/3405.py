def solution():
    shirts = 10  # James has 10 shirts
    pants = 12  # James has 12 pairs of pants
    shirt_time = 1.5  # It takes 1.5 hours to fix a shirt
    pants_time = 2 * shirt_time  # It takes twice as long to fix a pair of pants
    hourly_rate = 30  # The tailor charges $30 per hour

    # Calculate the total time required to fix all the shirts and pants
    total_time = shirts * shirt_time + pants * pants_time

    # Calculate the total cost of the tailor's services
    total_cost = total_time * hourly_rate
    result = total_cost
    return result

print(solution())