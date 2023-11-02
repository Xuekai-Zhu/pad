def solution():
    """Due to the restrictions of Coronavirus, Mr. Trent, the local store owner, increased the prices of goods at his store by 15% each to make the same income he was making before. If buying an orange was $40 and the price of purchasing a mango was $50, calculate how much it costs in total now to buy ten oranges and ten mangoes at the new prices."""
    orange_price = 40 * 1.15
    mango_price = 50 * 1.15
    total_cost = (orange_price * 10) + (mango_price * 10)
    result = total_cost
    return result

print(solution())