def solution():
    """Super Clean Car Wash Company cleans 80 cars per day. They make $5 per car washed. How much money will they make in 5 days?"""
    # Define the number of cars washed per day and the amount earned per car
    CARS_PER_DAY = 80
    AMOUNT_PER_CAR = 5

    # Calculate the total amount earned in 5 days
    total_cars_washed = CARS_PER_DAY * 5
    total_amount_earned = total_cars_washed * AMOUNT_PER_CAR

    # return the result
    result = total_amount_earned
    return result

print(solution())