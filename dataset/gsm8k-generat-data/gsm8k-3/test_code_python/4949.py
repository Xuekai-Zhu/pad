def solution():
    """Françoise sells pots of lily of the valley to fund humanitarian work. She buys them at €12 each and sells them at a 25% higher cost. How much will she give back to the association by selling 150 pots of lily of the valley?"""
    # Define the cost and selling price of each pot
    COST = 12
    SELLING_PRICE = COST * 1.25

    # Define the number of pots sold
    pots_sold = 150

    # Calculate Françoise's revenue from selling the pots
    revenue = pots_sold * SELLING_PRICE

    # Calculate Françoise's profit from selling the pots
    profit = revenue - (pots_sold * COST)

    # Calculate the amount Françoise will give back to the association
    association_share = profit * 0.8  # 80% of the profit goes to the association

    # Display the amount Françoise will give back to the association
    result = association_share
    return result

print(solution())