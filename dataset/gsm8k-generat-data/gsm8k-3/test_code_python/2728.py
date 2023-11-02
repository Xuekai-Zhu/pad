def solution():
    """A rancher has 340 head of cattle. He was about to sell them all for $204,000 when 172 of them fell sick and died. Because of the sickness, his customers lost confidence in his cattle, forcing him to lower his price by $150 per head. How much money would the devastated farmer lose if he sold the remaining cattle at the lowered price compared to the amount he would have made by selling them at the original price?"""
    # Define the original price per head and the new lowered price per head
    ORIGINAL_PRICE = 204000 / 340
    LOWERED_PRICE = ORIGINAL_PRICE - 150

    # Calculate the new number of healthy cattle
    healthy_cattle = 340 - 172

    # Calculate the amount the rancher would have made if he sold all the cattle at the original price
    original_earnings = 340 * ORIGINAL_PRICE

    # Calculate the amount the rancher would make if he sold the remaining healthy cattle at the lowered price
    lowered_earnings = healthy_cattle * LOWERED_PRICE

    # Calculate the amount of money the rancher would lose
    loss = original_earnings - lowered_earnings

    # Display the loss
    result = loss
    return result

print(solution())