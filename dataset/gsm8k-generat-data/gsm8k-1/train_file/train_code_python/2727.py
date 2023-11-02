def solution():
    """A rancher has 340 head of cattle. He was about to sell them all for $204,000 when 172 of them fell sick and died. Because of the sickness, his customers lost confidence in his cattle, forcing him to lower his price by $150 per head. How much money would the devastated farmer lose if he sold the remaining cattle at the lowered price compared to the amount he would have made by selling them at the original price?"""
    original_price_per_head = 600
    lowered_price_per_head = original_price_per_head - 150
    initial_sale_price = original_price_per_head * 340
    final_sale_price = lowered_price_per_head * (340-172)
    money_lost = initial_sale_price - final_sale_price
    result = money_lost
    return result

print(solution())