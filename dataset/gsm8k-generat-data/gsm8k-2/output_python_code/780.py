def solution():
    """I went to the music shop and there were CDs of The Life Journey for $100, A Day a Life for $50, and When You Rescind for $85 on display. If I bought 3 of each CD to share with my friends, what's the total amount of money I spent in the shop?"""
    cd1_price = 100
    cd2_price = 50
    cd3_price = 85
    num_cds = 3
    total_cost = (num_cds * cd1_price) + (num_cds * cd2_price) + (num_cds * cd3_price)
    result = total_cost
    return result

print(solution())