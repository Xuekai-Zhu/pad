def solution():
    """Samanta is planning a party for her friend Marta. She decided to raise some money among the guests she invited, to buy Marta a gift. Every participant gave Samanta $5 for this purpose and she herself put in $10. The gift cost was lower than expected, so there was $15 leftover. What was the price of the gift, if there were 12 guests invited?"""
    num_guests = 12
    total_money = num_guests * 5 + 10 + 15
    gift_price = total_money / num_guests
    result = gift_price
    return result

print(solution())