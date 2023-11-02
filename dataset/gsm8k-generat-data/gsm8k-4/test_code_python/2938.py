def solution():
    """Mike is saving up to buy a house. He puts away 10% of his $150,000 a year salary. He needs to save up 20% of the cost of a $450,000 house for a downpayment. How long will it take?"""
    # Define the annual salary
    annual_salary = 150000

    # Calculate the amount saved per year
    amount_saved_yearly = annual_salary * 0.1

    # Define the downpayment needed for the house
    downpayment = 450000 * 0.2

    # Calculate the number of years needed to save for the downpayment
    years_to_save = downpayment / amount_saved_yearly

    # Return the result
    result = int(years_to_save)
    return result

print(solution())