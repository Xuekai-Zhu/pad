def solution():
    """Morgan goes to the drive-thru and orders his lunch.  He gets a hamburger for $4, onion rings for $2 and a smoothie for $3. If he pays with a $20 bill, how much change does he receive?"""
    # Define the cost of each item
    HAMBURGER_PRICE = 4
    ONION_RINGS_PRICE = 2
    SMOOTHIE_PRICE = 3

    # Calculate the total cost of Morgan's lunch
    total_cost = HAMBURGER_PRICE + ONION_RINGS_PRICE + SMOOTHIE_PRICE

    # Calculate the change Morgan will receive
    change = 20 - total_cost

    # Display the change
    result = change
    return result

print(solution())