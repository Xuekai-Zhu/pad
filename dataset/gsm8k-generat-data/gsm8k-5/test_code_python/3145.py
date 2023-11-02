def solution():
    sailboat_rental_cost = 60  # Cost to rent a sailboat
    ski_boat_rental_cost = 80  # Cost per hour to rent a ski boat
    rental_duration = 3  # Rental duration in hours per day
    days_rented = 2  # Number of days rented

    # Calculate the total cost for Ken's sailboat rental
    ken_total_cost = sailboat_rental_cost * days_rented

    # Calculate the total cost for Aldrich's ski boat rental
    aldrich_total_cost = ski_boat_rental_cost * rental_duration * days_rented

    # Calculate the difference in cost between the two rentals
    cost_difference = aldrich_total_cost - ken_total_cost
    result = cost_difference
    return result

print(solution())