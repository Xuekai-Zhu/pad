def solution():
    """It will cost $60 to rent a sailboat and $80 per hour to rent a ski boat. Ken rented a sailboat while Aldrich rented a ski boat. How much more did it cost Aldrich to rent the ski boat than Ken to rent a sailboat for three hours a day in two days?"""
    sailboat_rental_cost = 60
    skiboat_rental_cost = 80
    rental_hours_per_day = 3
    rental_days = 2
    
    ken_total_cost = sailboat_rental_cost * rental_days
    aldrich_total_cost = (skiboat_rental_cost * rental_hours_per_day * rental_days) + sailboat_rental_cost * rental_days
    
    difference = aldrich_total_cost - ken_total_cost
    result = difference
    
    return result

print(solution())