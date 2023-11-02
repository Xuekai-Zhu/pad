def solution():
    """Toby held a garage sale to raise money to support friends who have lost their jobs. Of all the items that he sold during the garage sale, three of the items he sold made up 75% of the total amount of sales money he earned. He sold a treadmill for $100, a chest of drawers for half as much as he made for selling the treadmill, and he sold a television for three times what he earned for selling the treadmill. What is the total sum of money, in dollars, that Toby made at the garage sale?"""
    # Define the price of the treadmill and the chest of drawers
    treadmill_price = 100
    chest_price = treadmill_price / 2

    # Calculate the price of the television
    tv_price = treadmill_price * 3

    # Calculate the total amount of sales money Toby earned from the 3 items
    top_items_total = treadmill_price + chest_price + tv_price

    # Calculate the total amount of sales money Toby earned from all the items
    total_sales_money = top_items_total / 0.75

    result = total_sales_money
    return result

print(solution())