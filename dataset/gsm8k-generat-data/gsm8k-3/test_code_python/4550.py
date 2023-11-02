def solution():
    """Johannes owns a vegetable shop, he sells cabbage for $2 per kilogram. If Johannes was able to earn $30 last Wednesday, $24 last Friday, and $42 today, how many kilograms of cabbage was he able to sell?"""
    # Define the price per kilogram of cabbage
    PRICE_PER_KG = 2

    # Define the total amount earned for the three days
    total_earned = 30 + 24 + 42

    # Calculate the total weight of cabbage sold
    total_weight = total_earned / PRICE_PER_KG

    # Display the total weight of cabbage sold
    result = total_weight
    return result

print(solution())