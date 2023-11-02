def solution():
    """Dirk sells amulets at a Ren Faire. He sells for 2 days and each day he sells 25 amulets. Each amulet sells for 40 dollars and they cost him 30 dollars to make. If he has to give 10% of his revenue to the faire, how much profit did he make?"""
    # Define the number of amulets sold and the selling price
    amulets_sold = 25 * 2
    selling_price = 40

    # Calculate the revenue from selling amulets
    revenue = amulets_sold * selling_price

    # Calculate the cost of making amulets
    cost = amulets_sold * 30

    # Calculate the faire fee
    faire_fee = revenue * 0.1

    # Calculate the profit after deducting the cost and faire fee from revenue
    profit = revenue - cost - faire_fee

    result = profit
    return result

print(solution())