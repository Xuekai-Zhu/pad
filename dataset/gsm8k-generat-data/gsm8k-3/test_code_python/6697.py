def solution():
    """Renne earns $4000 per month and wants to save half of her monthly earnings to buy the vehicle of her dreams worth $16000. How many months of saving will it take her to buy the vehicle?"""
    # Define Renne's monthly earnings and savings rate
    monthly_earnings = 4000
    savings_rate = 0.5

    # Define the cost of the vehicle
    vehicle_cost = 16000

    # Calculate Renne's monthly savings
    monthly_savings = monthly_earnings * savings_rate

    # Calculate the number of months it will take to save enough for the vehicle
    months_to_save = vehicle_cost / monthly_savings

    # Display the number of months
    result = months_to_save
    return result

print(solution())