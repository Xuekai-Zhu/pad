def solution():
    """James sells a $500,000 house for 20% over market value. He splits the revenue with his 3 brothers. How much does each person get after taxes take away 10%?"""
    # Define the selling price of the house and the revenue after the market value increase
    house_price = 500000
    selling_price = house_price * 1.2

    # Calculate the total revenue shared among James and his 3 brothers
    total_revenue = selling_price / 4

    # Calculate the revenue after taxes are taken away
    revenue_after_tax = total_revenue * 0.9

    # Calculate the revenue after taxes for each person
    revenue_per_person = revenue_after_tax / 4

    # return the result
    result = round(revenue_per_person, 2)
    return result

print(solution())