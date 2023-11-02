def solution():
    """Toby held a garage sale to raise money to support friends who have lost their jobs. Of all the items that he sold during the garage sale, three of the items he sold made up 75% of the total amount of sales money he earned. He sold a treadmill for $100, a chest of drawers for half as much as he made for selling the treadmill, and he sold a television for three times what he earned for selling the treadmill. What is the total sum of money, in dollars, that Toby made at the garage sale?"""
    treadmill_price = 100
    chest_of_drawers_price = 0.5 * treadmill_price
    television_price = 3 * treadmill_price
    sum_of_top_3_items = treadmill_price + chest_of_drawers_price + television_price
    total_sales = sum_of_top_3_items / 0.75
    result = total_sales
    return result

print(solution())