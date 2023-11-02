def solution():
    # Define the original price of the book
    price = 400

    # Calculate the new price after a 15% decrease
    price = price - (0.15 * price)

    # Calculate the final price after a 40% increase
    price = price + (0.40 * price)

    result = price
    return result

print(solution())