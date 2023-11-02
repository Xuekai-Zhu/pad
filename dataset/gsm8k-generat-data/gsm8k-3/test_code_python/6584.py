def solution():
    """In a shopping mall, one T-shirt costs $20 each; a pair of pants costs $80; a pair of shoes costs $150. All items will get a 10% discount. How much does Eugene have to pay if he buys four T-shirts, three pairs of pants, and two pairs of shoes?"""
    # Define the prices of each item
    SHIRT_PRICE = 20
    PANTS_PRICE = 80
    SHOES_PRICE = 150

    # Define the quantities purchased
    shirts = 4
    pants = 3
    shoes = 2

    # Calculate the subtotal before discount
    subtotal = (shirts * SHIRT_PRICE) + (pants * PANTS_PRICE) + (shoes * SHOES_PRICE)

    # Calculate the discount
    discount = 0.1 * subtotal

    # Calculate the total cost after discount
    total_cost = subtotal - discount

    # Display the total cost
    result = total_cost
    return result

print(solution())