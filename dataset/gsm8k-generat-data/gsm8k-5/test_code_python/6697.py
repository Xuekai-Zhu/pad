def solution():
    monthly_income = 4000  # Renne earns $4000 per month
    savings_percentage = 0.5  # Renne wants to save half of her monthly earnings
    vehicle_cost = 16000  # The vehicle Renne wants to buy costs $16000

    # Calculate Renne's monthly savings
    monthly_savings = monthly_income * savings_percentage

    # Calculate the number of months it will take Renne to save enough for the vehicle
    months_to_save = vehicle_cost / monthly_savings

    result = months_to_save
    return result

print(solution())