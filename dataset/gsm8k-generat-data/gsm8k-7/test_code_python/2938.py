def solution():
    annual_salary = 150000
    savings_percent = 0.1  # 10% of salary saved each year
    house_cost = 450000
    downpayment_percent = 0.2  # 20% of house cost needed for downpayment

    # Calculate the amount Mike saves each year
    savings_amount = annual_salary * savings_percent

    # Calculate the amount needed for the downpayment
    downpayment_amount = house_cost * downpayment_percent

    # Calculate the number of years needed to save for the downpayment
    num_years = downpayment_amount / savings_amount
    result = num_years
    return result

print(solution())