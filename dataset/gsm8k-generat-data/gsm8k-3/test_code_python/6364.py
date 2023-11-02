def solution():
    """Toby held a garage sale to raise money to support friends who have lost their jobs.  Of all the items that he sold during the garage sale, three of the items he sold made up 75% of the total amount of sales money he earned.  He sold a treadmill for $100, a chest of drawers for half as much as he made for selling the treadmill, and he sold a television for three times what he earned for selling the treadmill.  What is the total sum of money, in dollars, that Toby made at the garage sale?"""
    # Calculate the amount of money made from selling the treadmill
    treadmill_sale = 100

    # Calculate the amount of money made from selling the chest of drawers
    chest_of_drawers_sale = treadmill_sale / 2

    # Calculate the amount of money made from selling the television
    television_sale = treadmill_sale * 3

    # Calculate the total amount of money made from selling these three items
    total_sales = treadmill_sale + chest_of_drawers_sale + television_sale

    # Calculate the total amount of money made from all items sold at the garage sale
    total_sales_percent = 0.75
    total_sales_amount = total_sales / total_sales_percent

    # Calculate the total amount of money Toby made at the garage sale
    total_amount = total_sales_amount

    # Display the total amount of money made
    result = total_amount
    return result

print(solution())