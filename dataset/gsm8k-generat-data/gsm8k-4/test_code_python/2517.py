def solution():
    """Mrs. Choi purchased a house for $80000. Five years later, she sold it for a 20% profit and got a 5% broker's commission from the original price. How much did the house sell for?"""
    # Define the original purchase price of the house
    original_price = 80000

    # Calculate the selling price after a 20% profit
    selling_price = original_price * 1.2

    # Calculate the commission paid to the broker
    commission = original_price * 0.05

    # Calculate the final selling price after commission
    final_price = selling_price - commission

    result = final_price
    return result

print(solution())