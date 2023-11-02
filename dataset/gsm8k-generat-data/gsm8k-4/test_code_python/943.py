def solution():
    """Javier is selling donuts to raise money for a new game. He wants to raise $96. He buys each dozen donuts for $2.40 and then sells each donut for $1. How many dozen donuts does he need to buy and sell to reach his goal?"""
    # Define the cost and selling price of one donut
    COST_PER_DOZEN = 2.40
    SELLING_PRICE_PER_DONUT = 1.00

    # Define the target amount to be raised
    TARGET_AMOUNT = 96.00

    # Calculate the number of donuts needed to be sold
    donuts_sold = TARGET_AMOUNT / SELLING_PRICE_PER_DONUT

    # Calculate the number of dozens needed to be purchased
    dozens_purchased = donuts_sold / 12

    # Round up to the nearest whole number
    dozens_purchased = math.ceil(dozens_purchased)

    # Calculate the total cost of purchasing the donuts
    total_cost = dozens_purchased * COST_PER_DOZEN

    # Check if the total cost is less than or equal to the target amount
    if total_cost <= TARGET_AMOUNT:
        result = dozens_purchased
    else:
        result = "Not possible to reach the target amount with the given cost per dozen and selling price per donut."

    return result

print(solution())