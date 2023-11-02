def solution():
    """James sells a $500,000 house for 20% over market value.  He splits the revenue with his 3 brothers.  How much does each person get after taxes take away 10%?"""
    # Calculate the sale price of the house
    sale_price = 500000 * 1.2

    # Calculate the revenue split between the four brothers
    split_revenue = sale_price / 4

    # Calculate the amount of taxes taken away
    tax_amount = split_revenue * 0.1

    # Calculate the amount each person gets after taxes
    net_earnings = (split_revenue - tax_amount) / 4

    # Display the net earnings for each person
    result = net_earnings
    return result

print(solution())