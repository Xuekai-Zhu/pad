def solution():
    """James buys 3 packs of candy.  He pays with a $20 bill and gets $11 change.  How much did each pack of candy cost?"""
    # Define the amount paid by James
    amount_paid = 20 - 11

    # Define the number of packs of candy purchased
    candy_packs = 3

    # Calculate the cost per candy pack
    cost_per_pack = amount_paid / candy_packs

    # Display the cost per candy pack
    result = cost_per_pack
    return result

print(solution())