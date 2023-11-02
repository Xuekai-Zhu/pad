def solution():
    """Mike is saving up to buy a house.  He puts away 10% of his $150,000 a year salary.  He needs to save up 20% of the cost of a $450,000 house for a downpayment.  How long will it take?"""
    # Calculate Mike's yearly savings
    yearly_savings = 0.1 * 150000

    # Calculate the downpayment amount on the house
    downpayment = 0.2 * 450000

    # Calculate the number of years it will take to save up for the downpayment
    years_to_save = downpayment / yearly_savings

    # Display the number of years
    result = years_to_save
    return result

print(solution())