def solution():
    customers_per_month = 500  # Village Foods gets 500 customers per month
    lettuce_price = 1  # Each head of lettuce costs $1
    tomatoes_price = 0.5  # Each tomato costs $0.5
    lettuce_per_customer = 2  # Each customer purchases 2 heads of lettuce
    tomatoes_per_customer = 4  # Each customer purchases 4 tomatoes

    # Calculate the total sales of lettuce and tomatoes per customer
    sales_per_customer = (lettuce_price * lettuce_per_customer) + (tomatoes_price * tomatoes_per_customer)

    # Calculate the total sales of lettuce and tomatoes per month
    total_sales = sales_per_customer * customers_per_month
    result = total_sales
    return result

print(solution())