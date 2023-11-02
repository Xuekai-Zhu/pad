def solution():
    """Barry goes to a shop to buy a shirt he'd been admiring for quite some time. He tells the attendant that it's his birthday so she decides to give him a 15% special discount. The price tag on the shirt says $80. How much is he supposed to pay now, considering the special discount?"""
    # Define the original price of the shirt
    original_price = 80

    # Calculate the amount of the discount
    discount = original_price * 0.15

    # Calculate the new price
    new_price = original_price - discount

    # Display the new price
    result = new_price
    return result

print(solution())