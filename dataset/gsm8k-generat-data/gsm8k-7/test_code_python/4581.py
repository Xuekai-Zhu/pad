def solution():
    gallons_per_day = 200
    days_in_june = 30
    price_per_gallon = 3.55
    expenses_per_month = 3000

    # Calculate the total number of gallons produced in June
    total_gallons = gallons_per_day * days_in_june

    # Calculate the total income from selling all the milk
    total_income = total_gallons * price_per_gallon

    # Subtract the expenses to get the net income
    net_income = total_income - expenses_per_month
    result = net_income
    return result

print(solution())