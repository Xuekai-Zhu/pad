def solution():
    # Calculate Mike's yearly savings
    yearly_savings = 0.1 * 150000  # 10% of his $150,000 salary

    # Calculate the amount of money Mike needs to save for a downpayment
    downpayment = 0.2 * 450000  # 20% of the cost of the house

    # Calculate the number of years it will take for Mike to save up for the downpayment
    years_to_save = downpayment // yearly_savings
    result = years_to_save
    return result

print(solution())