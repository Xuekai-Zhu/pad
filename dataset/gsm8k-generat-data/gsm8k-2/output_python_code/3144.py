def solution():
    """It will cost $60 to rent a sailboat and $80 per hour to rent a ski boat. Ken rented a sailboat while Aldrich rented a ski boat. How much more did it cost Aldrich to rent the ski boat than Ken to rent a sailboat for three hours a day in two days?"""
    sailboat_rental = 60
    ski_boat_rental = 80
    rental_time = 3
    rental_days = 2

    ken_cost = sailboat_rental * rental_days
    aldrich_cost = ski_boat_rental * rental_time * rental_days

    cost_difference = aldrich_cost - ken_cost
    result = cost_difference
    return result

print(solution())