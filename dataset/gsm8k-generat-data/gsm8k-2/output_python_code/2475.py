def solution():
    """Super Clean Car Wash Company cleans 80 cars per day. They make $5 per car washed. How much money will they make in 5 days?"""
    cars_per_day = 80
    revenue_per_car = 5
    total_days = 5
    total_cars = cars_per_day * total_days
    total_revenue = total_cars * revenue_per_car
    result = total_revenue
    return result

print(solution())