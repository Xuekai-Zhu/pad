def solution():
    """Faraday owns a flower shop. He sells a sunflower that costs $2 each and a bouquet of sunflower that costs $8. If Faraday earned $26 from the sunflower and $56 from the bouquet per day, and if each bouquet has 12 sunflowers, how many sunflowers was Faraday able to sell after 3 days?"""
    sunflower_price = 2
    bouquet_price = 8
    bouquet_sunflowers = 12
    sunflower_profit = 26
    bouquet_profit = 56
    total_profit = sunflower_profit + bouquet_profit
    total_sunflowers = ((sunflower_profit / sunflower_price) + (bouquet_profit / bouquet_price) * bouquet_sunflowers) * 3
    result = total_sunflowers
    return result

print(solution())