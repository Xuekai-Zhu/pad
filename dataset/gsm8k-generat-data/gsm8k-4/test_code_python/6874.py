def solution():
    """Mandy’s phone data plan charges $30 per month for data. Her first month, she got a promotional rate of one-third the normal price. However, in the fourth month she went over her data limit and was charged an extra fee of $15. How much did Mandy pay in the first 6 months for data?"""
    # Define the cost of regular data plan and the promotional rate for the first month
    regular_price = 30
    promo_price = regular_price / 3

    # Calculate Mandy's total cost for the first three months
    first_three_months = promo_price + (regular_price * 2)

    # Add the extra fee for the fourth month
    fourth_month = regular_price + 15

    # Add the cost for the fifth and sixth months
    fifth_month = regular_price
    sixth_month = regular_price

    # Calculate the total cost for the first 6 months
    total_cost = first_three_months + fourth_month + fifth_month + sixth_month

    result = total_cost
    return result

print(solution())