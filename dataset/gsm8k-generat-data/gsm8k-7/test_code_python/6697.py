def solution():
    monthly_earnings = 4000
    savings_percentage = 0.5
    vehicle_price = 16000

    # Calculate the amount Renne will save per month
    monthly_savings = monthly_earnings * savings_percentage

    # Calculate the total number of months it will take Renne to save enough to buy the vehicle
    months_to_save = vehicle_price / monthly_savings

    result = months_to_save
    return result

print(solution())