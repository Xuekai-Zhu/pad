def solution():
    """In a shopping mall, one T-shirt costs $20 each; a pair of pants costs $80; a pair of shoes costs $150. All items will get a 10% discount. How much does Eugene have to pay if he buys four T-shirts, three pairs of pants, and two pairs of shoes?"""
    # Define the prices of the items
    tshirt_price = 20
    pants_price = 80
    shoes_price = 150

    # Define the number of items purchased
    num_tshirts = 4
    num_pants = 3
    num_shoes = 2

    # Calculate the total price before discount
    total_price = (tshirt_price * num_tshirts) + (pants_price * num_pants) + (shoes_price * num_shoes)

    # Calculate the discount
    discount = total_price * 0.1

    # Calculate the final price
    final_price = total_price - discount

    result = final_price
    return result

print(solution())