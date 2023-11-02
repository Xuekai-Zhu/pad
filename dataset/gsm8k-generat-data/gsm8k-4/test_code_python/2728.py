def solution():
    """A rancher has 340 head of cattle. He was about to sell them all for $204,000 when 172 of them fell sick and died. Because of the sickness, his customers lost confidence in his cattle, forcing him to lower his price by $150 per head. How much money would the devastated farmer lose if he sold the remaining cattle at the lowered price compared to the amount he would have made by selling them at the original price?"""
    # Define the initial number of cattle and the original price per head
    initial_cattle = 340
    original_price = 600

    # Calculate the total value of the initial herd
    initial_value = initial_cattle * original_price

    # Calculate the number of remaining cattle and the lowered price per head
    remaining_cattle = initial_cattle - 172
    lowered_price = original_price - 150

    # Calculate the total value of the remaining herd at the lowered price
    remaining_value = remaining_cattle * lowered_price

    # Calculate the lost value due to the lowered price
    lost_value = initial_value - remaining_value

    result = lost_value
    return result

print(solution())