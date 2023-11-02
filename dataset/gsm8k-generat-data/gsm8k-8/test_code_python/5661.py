def solution():
    # Calculate the total revenue from pancake sales
    pancake_price = 4
    pancake_sales = 60
    pancake_revenue = pancake_price * pancake_sales

    # Calculate the total revenue from bacon sales
    bacon_price = 2
    bacon_sales = 90
    bacon_revenue = bacon_price * bacon_sales

    # Calculate the total revenue from the fundraiser
    total_revenue = pancake_revenue + bacon_revenue
    result = total_revenue
    return result

print(solution())