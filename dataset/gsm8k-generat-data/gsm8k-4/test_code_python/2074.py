def solution():
    """Samanta is planning a party for her friend Marta. She decided to raise some money among the guests she invited, to buy Marta a gift. Every participant gave Samanta $5 for this purpose and she herself put in $10. The gift cost was lower than expected, so there was $15 leftover. What was the price of the gift, if there were 12 guests invited?"""
    # Define the number of guests and the amount Samanta contributed
    num_guests = 12
    samanta_contribution = 10

    # Calculate the total amount collected from the guests
    total_guest_contribution = num_guests * 5

    # Calculate the total amount available for the gift
    total_gift_amount = samanta_contribution + total_guest_contribution + 15

    # Calculate the price of the gift
    gift_price = total_gift_amount / num_guests

    result = gift_price
    return result

print(solution())