def solution():
    lawn_price = 33
    num_lawns = 16
    tip_amount = 10
    num_customers_with_tip = 3

    # Calculate the total amount earned from mowing lawns
    total_lawn_earnings = lawn_price * num_lawns

    # Calculate the total amount earned in tips
    total_tip_earnings = tip_amount * num_customers_with_tip

    # Calculate the total earnings from mowing lawns last week
    total_earnings = total_lawn_earnings + total_tip_earnings
    result = total_earnings
    return result

print(solution())