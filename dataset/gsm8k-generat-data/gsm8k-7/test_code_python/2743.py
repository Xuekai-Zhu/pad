def solution():
    num_items = 2000
    retail_price = 50
    discount = 0.8
    sell_percentage = 0.9
    creditors_debt = 15000

    # Calculate the total revenue from the sale after the discount
    revenue = num_items * retail_price * discount

    # Calculate the total amount of items sold
    num_items_sold = num_items * sell_percentage

    # Calculate the total cost of goods sold
    cost_of_goods_sold = num_items_sold * (retail_price * discount)

    # Calculate the amount left after paying creditors
    left_over_money = revenue - cost_of_goods_sold - creditors_debt
    result = left_over_money
    return result

print(solution())