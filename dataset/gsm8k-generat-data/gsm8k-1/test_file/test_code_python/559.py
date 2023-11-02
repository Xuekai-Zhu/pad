def solution():
    """James decides to buy birthday candles for his 2 sons. One of them is 12 and the other is 4 years younger. A pack of 5 candles costs $3. How much does James spend on candles?"""
    son1_age = 12
    son2_age = son1_age - 4
    total_candles = son1_age + son2_age
    candles_per_pack = 5
    packs_needed = total_candles // candles_per_pack + (1 if total_candles % candles_per_pack != 0 else 0)
    price_per_pack = 3
    total_price = packs_needed * price_per_pack
    result = total_price
    return result

print(solution())