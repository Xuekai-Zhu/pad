def solution():
    base_salary = 3000
    num_houses_sold = 3
    total_earnings = 8000

    # Calculate the total earnings from commissions
    total_commission_earnings = total_earnings - base_salary

    # Calculate the average commission rate for each house sold
    avg_commission_rate = total_commission_earnings / num_houses_sold

    # Calculate the total sale price for all houses sold
    total_sale_price = total_earnings / avg_commission_rate

    # Calculate the sale price of House C
    house_c_price = (total_sale_price - 110000) / 2

    # Calculate the sale price of House B
    house_b_price = house_c_price * 3

    # Calculate the sale price of House A
    house_a_price = total_sale_price - house_c_price - house_b_price

    result = house_a_price
    return result

print(solution())