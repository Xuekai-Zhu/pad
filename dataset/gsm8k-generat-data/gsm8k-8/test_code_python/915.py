def solution():
    # Calculate the total power used by all the bulbs in one day
    total_power = 60 * 40 

    # Calculate the monthly power usage
    monthly_power = total_power * 30 

    # Calculate the electricity bill for the month
    electricity_bill = monthly_power * 0.20

    result = electricity_bill
    return result

print(solution())