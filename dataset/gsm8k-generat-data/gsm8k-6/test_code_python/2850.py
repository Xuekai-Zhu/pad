def solution():
    monthly_income = 2000  # Mr. John's monthly income
    transport_fare = monthly_income * 0.05  # Mr. John spends 5% of his income on transport
    money_left = monthly_income - transport_fare  # Calculate the money Mr. John has left after deducting his transport fare
    result = money_left
    return result

print(solution())