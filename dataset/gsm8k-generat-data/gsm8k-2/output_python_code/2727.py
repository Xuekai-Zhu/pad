def solution():
    """A rancher has 340 head of cattle. He was about to sell them all for $204,000 when 172 of them fell sick and died. Because of the sickness, his customers lost confidence in his cattle, forcing him to lower his price by $150 per head. How much money would the devastated farmer lose if he sold the remaining cattle at the lowered price compared to the amount he would have made by selling them at the original price?"""
    original_price_per_head = 204000 / (340 - 172)
    lowered_price_per_head = original_price_per_head - 150
    remaining_cattle = 340 - 172
    original_revenue = remaining_cattle * original_price_per_head
    lowered_revenue = remaining_cattle * lowered_price_per_head
    loss = original_revenue - lowered_revenue
    result = loss
    return result

print(solution())