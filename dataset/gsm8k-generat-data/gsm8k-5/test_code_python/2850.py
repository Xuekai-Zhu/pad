def solution():
    monthly_income = 2000  # Mr. John's monthly income is $2000
    transport_fare = monthly_income * 0.05  # Mr. John spends 5% of his income on transport

    # Calculate Mr. John's income after deducting transport fare
    income_after_transport = monthly_income - transport_fare
    result = income_after_transport
    return result

print(solution())