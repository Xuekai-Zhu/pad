def solution():
    """Fred spent half of his allowance going to the movies. He washed the family car and earned 6 dollars. What is his weekly allowance if he ended with 14 dollars?"""
    ending_allowance = 14
    car_wash_earnings = 6
    remaining_allowance = ending_allowance - car_wash_earnings
    weekly_allowance = remaining_allowance * 2
    result = weekly_allowance
    return result

print(solution())