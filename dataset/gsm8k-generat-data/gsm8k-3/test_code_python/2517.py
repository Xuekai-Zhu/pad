def solution():
    """Mrs. Choi purchased a house for $80000. Five years later, she sold it for a 20% profit and got a 5% broker's commission from the original price. How much did the house sell for?"""
    # Define the original purchase price and the profit percentage
    PURCHASE_PRICE = 80000
    PROFIT_PERCENTAGE = 20

    # Calculate the selling price before commission
    selling_price = PURCHASE_PRICE * (1 + PROFIT_PERCENTAGE / 100)

    # Calculate the commission amount
    commission_amount = PURCHASE_PRICE * 0.05

    # Calculate the final selling price
    final_price = selling_price - commission_amount

    # Display the final selling price
    result = final_price
    return result

print(solution())