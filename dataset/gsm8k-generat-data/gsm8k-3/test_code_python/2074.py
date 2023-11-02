def solution():
    """Samanta is planning a party for her friend Marta. She decided to raise some money among the guests she invited, to buy Marta a gift. Every participant gave Samanta $5 for this purpose and she herself put in $10. The gift cost was lower than expected, so there was $15 leftover. What was the price of the gift, if there were 12 guests invited?"""
    # Define the amount contributed by each guest and Samanta
    CONTRIBUTION_PER_PERSON = 5
    SAMANTA_CONTRIBUTION = 10

    # Define the total number of guests and their contributions
    total_guests = 12
    total_contributions = (total_guests * CONTRIBUTION_PER_PERSON) + SAMANTA_CONTRIBUTION

    # Define the amount leftover after buying the gift
    leftover_amount = 15

    # Calculate the price of the gift
    gift_price = total_contributions - leftover_amount

    # Display the price of the gift
    result = gift_price
    return result

print(solution())