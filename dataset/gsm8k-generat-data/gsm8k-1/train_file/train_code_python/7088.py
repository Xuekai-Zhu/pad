def solution():
    """Zach rented a car for $150 plus 50 cents for each mile. He drove 620 miles on Monday and another 744 miles on Thursday. How much did he spend?"""
    rental_cost = 150
    monday_miles = 620
    thursday_miles = 744
    miles_driven = monday_miles + thursday_miles
    cost_per_mile = 0.5
    total_cost = rental_cost + (miles_driven * cost_per_mile)
    result = total_cost
    return result

print(solution())