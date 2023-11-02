def solution():
    # Calculate the total sales of lettuce and tomatoes per customer
    sales_per_customer = (2 * 1) + (4 * 0.5)  # 2 heads of lettuce for $1 each and 4 tomatoes for $0.5 apiece

    # Calculate the total sales of lettuce and tomatoes for all 500 customers
    total_sales = sales_per_customer * 500

    result = total_sales
    return result

print(solution())