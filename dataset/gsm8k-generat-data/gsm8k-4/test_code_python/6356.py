def solution():
    """Morgan goes to the drive-thru and orders his lunch. He gets a hamburger for $4, onion rings for $2 and a smoothie for $3. If he pays with a $20 bill, how much change does he receive?"""
    # Define the prices of the items
    hamburger_price = 4
    onion_rings_price = 2
    smoothie_price = 3

    # Calculate the total cost of the order
    total_cost = hamburger_price + onion_rings_price + smoothie_price

    # Calculate the change Morgan will receive
    change = 20 - total_cost

    result = change
    return result

print(solution())