def solution():
    """At the Delicious Delhi restaurant, Hilary bought three samosas at $2 each and four orders of pakoras, at $3 each, and a mango lassi, for $2. She left a 25% tip. How much did the meal cost Hilary, with tax, in dollars?"""
    # Define the prices of each item
    SAMOSA_PRICE = 2
    PAKORA_PRICE = 3
    LASSI_PRICE = 2
    TIP_MULTIPLIER = 0.25

    # Calculate the cost of the samosas
    samosa_cost = 3 * SAMOSA_PRICE

    # Calculate the cost of the pakoras
    pakora_cost = 4 * PAKORA_PRICE

    # Calculate the cost of the lassi
    lassi_cost = LASSI_PRICE

    # Calculate the subtotal
    subtotal = samosa_cost + pakora_cost + lassi_cost

    # Calculate the tip
    tip = TIP_MULTIPLIER * subtotal

    # Calculate the total
    total = subtotal + tip

    # Display the total cost
    result = total
    return result

print(solution())