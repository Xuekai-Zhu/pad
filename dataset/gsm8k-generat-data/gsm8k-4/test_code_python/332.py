def solution():
    """Dorothy earns $60000 a year from her work. She needs to pay 18% of this amount in taxes. How much money will she have left after she pays the taxes?"""
    # Define Dorothy's annual income and tax rate
    annual_income = 60000
    tax_rate = 0.18

    # Calculate the amount of taxes Dorothy needs to pay
    taxes = annual_income * tax_rate

    # Calculate Dorothy's take-home pay after taxes
    take_home_pay = annual_income - taxes

    # return the result
    result = take_home_pay
    return result

print(solution())