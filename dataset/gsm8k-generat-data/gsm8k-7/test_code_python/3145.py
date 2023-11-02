def solution():
    sailboat_rental_cost = 60
    ski_boat_rental_cost = 80
    rental_duration = 3 # in hours
    num_days = 2

    # Calculate the total cost of sailboat rentals
    total_sailboat_cost = sailboat_rental_cost * num_days

    # Calculate the total cost of ski boat rentals
    total_ski_boat_cost = (ski_boat_rental_cost * rental_duration * num_days)

    # Calculate the difference in cost between renting a ski boat and a sailboat
    cost_difference = total_ski_boat_cost - total_sailboat_cost
    result = cost_difference
    return result

print(solution())