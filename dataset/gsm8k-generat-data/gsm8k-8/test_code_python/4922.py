def solution():
    # Calculate the sale price of the house
    sale_price = 500000 * 1.2

    # Calculate the total revenue split between the 4 brothers
    total_revenue = sale_price / 4

    # Calculate the amount taken away by taxes
    taxes = total_revenue * 0.1

    # Calculate the amount each person gets after taxes
    amount_each_person_gets = (total_revenue - taxes) / 4

    result = amount_each_person_gets
    return result

print(solution())