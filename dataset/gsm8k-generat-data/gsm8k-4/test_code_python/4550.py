def solution():
    """Johannes owns a vegetable shop, he sells cabbage for $2 per kilogram. If Johannes was able to earn $30 last Wednesday, $24 last Friday, and $42 today, how many kilograms of cabbage was he able to sell?"""
    # Define the price per kilogram of cabbage
    PRICE_PER_KG = 2

    # Calculate the total earnings from selling cabbage
    total_earnings = 30 + 24 + 42

    # Calculate the total weight of cabbage sold
    total_weight = total_earnings / PRICE_PER_KG

    result = total_weight
    return result

print(solution())