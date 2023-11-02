def solution():
    """Renne earns $4000 per month and wants to save half of her monthly earnings to buy the vehicle of her dreams worth $16000. How many months of saving will it take her to buy the vehicle?"""
    # Define Renne's monthly earnings and the cost of the vehicle
    monthly_earnings = 4000
    vehicle_cost = 16000

    # Calculate the amount Renne needs to save each month to reach her goal
    monthly_savings = vehicle_cost / 2

    # Calculate the number of months it will take Renne to save enough money
    saving_months = monthly_savings / (monthly_earnings / 2)

    # Round up to the nearest month and return the result
    result = round(saving_months)
    return result

print(solution())