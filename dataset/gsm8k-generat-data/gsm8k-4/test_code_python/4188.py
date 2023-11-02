def solution():
    """Barry goes to a shop to buy a shirt he'd been admiring for quite some time. He tells the attendant that it's his birthday so she decides to give him a 15% special discount. The price tag on the shirt says $80. How much is he supposed to pay now, considering the special discount?"""
    # Define the original price of the shirt and the discount percentage
    original_price = 80
    discount_percentage = 0.15

    # Calculate the discount amount
    discount_amount = original_price * discount_percentage

    # Calculate the new price after the discount
    new_price = original_price - discount_amount

    # return the result
    result = new_price
    return result

print(solution())