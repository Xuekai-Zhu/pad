def solution():
    """Fred spent half of his allowance going to the movies. He washed the family car and earned 6 dollars. What is his weekly allowance if he ended with 14 dollars?"""
    ending_amount = 14
    car_wash_earnings = 6
    remaining_amount = ending_amount - car_wash_earnings
    allowance_per_week = remaining_amount * 2
    result = allowance_per_week
    return result

print(solution())