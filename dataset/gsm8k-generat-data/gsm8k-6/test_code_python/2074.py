def solution():
    # Calculate the total amount of money collected by Samanta
    total_money = 12 * 5 + 10  # 12 guests gave $5 each, Samanta herself put in $10

    # Calculate the cost of the gift
    gift_cost = total_money - 15  # there was $15 leftover

    # Calculate the price of the gift
    price_of_gift = gift_cost / 12  # the cost was split among 12 guests

    result = price_of_gift
    return result

print(solution())