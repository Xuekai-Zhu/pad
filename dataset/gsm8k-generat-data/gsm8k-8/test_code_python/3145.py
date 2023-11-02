def solution():
    # Define the costs and rental time
    sailboat_cost = 60
    skiboat_cost = 80
    rental_time = 3
    num_days = 2

    # Calculate the total cost for Ken's sailboat rental
    ken_total_cost = sailboat_cost + (skiboat_cost * rental_time * num_days)

    # Calculate the total cost for Aldrich's ski boat rental
    aldrich_total_cost = (sailboat_cost * rental_time * num_days) + (skiboat_cost * rental_time * num_days)

    # Calculate the difference in cost
    difference = aldrich_total_cost - ken_total_cost
    result = difference
    return result

print(solution())