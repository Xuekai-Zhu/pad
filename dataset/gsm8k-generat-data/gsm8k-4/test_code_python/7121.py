def solution():
    """Jenny makes and freezes pans of lasagna all week so she can sell them at the market on the weekend. It costs Jenny $10.00 in ingredients to make 1 pan of lasagna. If she makes and sells 20 pans over the weekend at $25.00 apiece, how much does she make after factoring in expenses?"""
    # Define the cost of ingredients for one pan of lasagna
    COST_PER_PAN = 10

    # Define the selling price of one pan of lasagna
    PRICE_PER_PAN = 25

    # Define the number of pans of lasagna made and sold
    PANS_SOLD = 20

    # Calculate the total revenue
    revenue = PANS_SOLD * PRICE_PER_PAN

    # Calculate the total cost of ingredients
    cost = PANS_SOLD * COST_PER_PAN

    # Calculate the profit after factoring in expenses
    profit = revenue - cost

    # Return the result
    return profit

print(solution())