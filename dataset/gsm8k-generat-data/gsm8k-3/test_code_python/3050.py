def solution():
    """Janet bought some muffins at the bakery. Each muffin is 75 cents. Janet paid $20 and got $11 in change back. How many muffins did Janet buy?"""
    # Define the cost of each muffin
    MUFFIN_PRICE = 0.75

    # Calculate the total amount paid
    total_paid = 20 - 11

    # Calculate the number of muffins purchased
    num_muffins = int(total_paid / MUFFIN_PRICE)

    # Display the number of muffins purchased
    result = num_muffins
    return result

print(solution())