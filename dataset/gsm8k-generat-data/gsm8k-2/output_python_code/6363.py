def solution():
    """Toby held a garage sale to raise money to support friends who have lost their jobs. Of all the items that he sold during the garage sale, three of the items he sold made up 75% of the total amount of sales money he earned. He sold a treadmill for $100, a chest of drawers for half as much as he made for selling the treadmill, and he sold a television for three times what he earned for selling the treadmill. What is the total sum of money, in dollars, that Toby made at the garage sale?"""
    # calculate the amount of money made from selling the treadmill
    treadmill_price = 100
    # calculate the amount of money made from selling the chest of drawers
    chest_price = treadmill_price / 2
    # calculate the amount of money made from selling the television
    tv_price = treadmill_price * 3
    # calculate the total amount of money made from the top 3 items
    top_three_total = treadmill_price + chest_price + tv_price
    # calculate the total amount of money made from all items
    total_sales = top_three_total / 0.75
    result = total_sales
    return result

print(solution())