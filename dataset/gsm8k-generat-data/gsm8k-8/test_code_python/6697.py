def solution():
    monthly_earnings = 4000
    saving_percentage = 0.5
    vehicle_price = 16000

    # Calculate the amount Renne needs to save each month
    monthly_savings = monthly_earnings * saving_percentage

    # Calculate the number of months it will take to save for the vehicle
    saving_period = vehicle_price / monthly_savings
    result = saving_period
    return result

print(solution())