def solution():
    cars_per_day = 80  # Super Clean Car Wash Company cleans 80 cars per day
    price_per_car = 5  # The company makes $5 per car washed
    days = 5  # The company wants to know how much money they will make in 5 days

    # Calculate the total number of cars washed in 5 days
    total_cars_washed = cars_per_day * days

    # Calculate the total amount of money made in 5 days
    total_money_made = total_cars_washed * price_per_car
    result = total_money_made
    return result

print(solution())