def solution():
    """Selina is selling some of her old clothes to a second-hand store. They will buy her pants for $5 each, her shorts for $3 each, and her shirts for $4 each. She sells 3 pairs of pants, 5 pairs of shorts, and some shirts. After she gets her money, she sees 2 shirts that she likes which cost $10 each and buys them. She leaves the store with $30. How many shirts did she sell to the store?"""
    # Define the prices of each type of clothing
    PANTS_PRICE = 5
    SHORTS_PRICE = 3
    SHIRTS_PRICE = 4

    # Define the number of each type of clothing sold
    pants_num = 3
    shorts_num = 5

    # Calculate the total amount earned from selling pants and shorts
    pants_cost = pants_num * PANTS_PRICE
    shorts_cost = shorts_num * SHORTS_PRICE
    total_cost = pants_cost + shorts_cost

    # Calculate the amount spent on the two shirts Selina bought
    spent = 20  # 2 shirts at $10 each

    # Calculate the amount Selina received from selling shirts
    received = 30 - spent - total_cost

    # Calculate the number of shirts sold
    shirt_num = received // SHIRTS_PRICE

    # Display the number of shirts sold
    result = shirt_num
    return result

print(solution())