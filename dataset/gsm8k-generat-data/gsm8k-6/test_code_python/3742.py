def solution():
    # Calculate the total amount paid originally
    total_paid = 120

    # Calculate the total price of the pants
    pants_price = total_paid / 3

    # Calculate the total amount paid for the shirts
    shirt_price = (total_paid - (3 * pants_price)) / 2

    # Calculate the amount refunded when the pants are returned
    pants_refund = 0.25 * (3 * pants_price)

    # Calculate the final price of 1 shirt
    final_shirt_price = (total_paid - pants_refund - (2 * shirt_price)) / 2

    result = final_shirt_price
    return result

print(solution())