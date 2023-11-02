def solution():
    # Define the monthly income and percentage spent on transport
    monthly_income = 2000
    transport_percent = 0.05

    # Calculate the amount spent on transport
    transport_amount = monthly_income * transport_percent

    # Calculate the remaining amount after deducting transport fare
    remaining_amount = monthly_income - transport_amount
    result = remaining_amount
    return result

print(solution())