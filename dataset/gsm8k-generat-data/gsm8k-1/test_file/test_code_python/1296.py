def solution():
    """Josh runs a car shop and services 3 cars a day. He is open every day of the week except Sunday and Wednesday. He gets paid $4 per car. How much does he make in 2 weeks?"""
    cars_serviced_per_day = 3
    days_per_week = 5
    weeks = 2
    cars_serviced_in_two_weeks = cars_serviced_per_day * days_per_week * weeks
    price_per_car = 4
    total_earnings = cars_serviced_in_two_weeks * price_per_car
    result = total_earnings
    return result

print(solution())