def solution():
    # Calculate the total revenue from selling items
    retail_price = 50  # retail price of each item
    discount_percent = 80  # percent discount offered
    selling_price = (100 - discount_percent) / 100 * retail_price  # selling price after discount
    num_items = 2000  # total number of items
    num_sold = 0.9 * num_items  # percentage of items sold
    revenue = num_sold * selling_price  # total revenue from selling items

    # Calculate the money left after paying off creditors
    creditors_owed = 15000  # amount owed to creditors
    money_left = revenue - creditors_owed

    result = money_left
    return result

print(solution())