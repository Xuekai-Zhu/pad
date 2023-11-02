def solution():
    """Jenny makes and freezes pans of lasagna all week so she can sell them at the market on the weekend.
    It costs Jenny $10.00 in ingredients to make 1 pan of lasagna.  If she makes and sells 20 pans over the
    weekend at $25.00 apiece, how much does she make after factoring in expenses?"""
    
    # Define the cost and selling price per pan of lasagna
    INGREDIENT_COST = 10
    SELLING_PRICE = 25
    
    # Define the number of pans of lasagna made and sold
    pans_made = 20
    pans_sold = 20
    
    # Calculate the total cost of ingredients
    total_cost = pans_made * INGREDIENT_COST
    
    # Calculate the total revenue from selling the lasagnas
    total_revenue = pans_sold * SELLING_PRICE
    
    # Calculate the profit by subtracting the total cost from the total revenue
    profit = total_revenue - total_cost
    
    # Display the profit
    result = profit
    return result

print(solution())