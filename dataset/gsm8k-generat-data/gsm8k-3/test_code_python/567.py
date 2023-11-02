def solution():
    """Lilith originally had five dozen water bottles that she needed to sell at $2 each to get exactly enough money to buy her friend a birthday gift. However, at the store, Lilith realized she could not sell at $2 because the regular price was $1.85 per water bottle in her town, and she had to reduce her price to $1.85 as well to sell her water bottles. Calculate the total amount of money Lilith will have to find to buy her friend the birthday gift after selling her water bottles at the reduced cost."""
    # Define Lilith's original selling price per water bottle and the regular price in her town
    ORIGINAL_PRICE = 2
    REGULAR_PRICE = 1.85

    # Define the number of water bottles Lilith had
    bottle_count = 5 * 12

    # Calculate the total revenue from selling the water bottles at the reduced price
    revenue = bottle_count * REGULAR_PRICE

    # Calculate the amount of money Lilith needs to buy her friend the birthday gift after selling the water bottles
    gift_cost = revenue - (bottle_count * (REGULAR_PRICE - ORIGINAL_PRICE))

    # Display the total amount of money Lilith needs
    result = gift_cost
    return result

print(solution())