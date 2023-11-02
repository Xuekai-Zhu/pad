def solution():
    """Zach rented a car for $150 plus 50 cents for each mile. He drove 620 miles on Monday and another 744 miles on Thursday. How much did he spend?"""
    rental_fee = 150
    mileage_cost = 0.5
    monday_miles = 620
    thursday_miles = 744
    total_miles = monday_miles + thursday_miles
    total_cost = rental_fee + (total_miles * mileage_cost)
    result = total_cost
    return result

print(solution())