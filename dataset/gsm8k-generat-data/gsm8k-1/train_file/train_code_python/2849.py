def solution():
    """Mr. John works at a shopping mall and receives a monthly income of $2000, but he spends approximately 5% of this amount on public transport to and from the mall in a month. How much will he have left after deducting his monthly transport fare from his income?"""
    monthly_income = 2000
    transport_fare_percentage = 5
    transport_fare = (transport_fare_percentage / 100) * monthly_income
    remaining_income = monthly_income - transport_fare
    result = remaining_income
    return result

print(solution())