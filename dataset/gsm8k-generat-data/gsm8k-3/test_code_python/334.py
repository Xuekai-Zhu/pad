def solution():
    """Dorothy earns $60000 a year from her work. She needs to pay 18% of this amount in taxes. How much money will she have left after she pays the taxes?"""
    # Define Dorothy's annual income
    income = 60000

    # Define the tax rate
    tax_rate = 0.18

    # Calculate Dorothy's tax amount
    tax_amount = income * tax_rate

    # Calculate Dorothy's net income after taxes
    net_income = income - tax_amount

    # Display Dorothy's net income after taxes
    result = net_income
    return result

print(solution())