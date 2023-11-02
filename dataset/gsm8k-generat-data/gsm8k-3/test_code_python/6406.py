def solution():
    """Enrico owns a rooster farm, he sells each rooster for $0.50 per kilogram. He was able to sell a 30-kilogram rooster and a 40-kilogram rooster, how much money was he able to earn?"""
    # Define the price per kilogram of roosters
    PRICE_PER_KG = 0.5

    # Define the weights of the two roosters
    weight1 = 30
    weight2 = 40

    # Calculate the total earnings from selling the two roosters
    earnings = (weight1 + weight2) * PRICE_PER_KG

    # Display the total earnings
    result = earnings
    return result

print(solution())