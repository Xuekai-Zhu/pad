def solution():
    """Hendricks buys a guitar for $200, which is 20% less than what Gerald bought the same guitar for. How much did Gerald pay for his guitar?"""
    # Define the price Hendricks paid for the guitar
    hendricks_price = 200

    # Calculate the price Gerald paid for the guitar
    gerald_price = hendricks_price / (1 - 0.2)

    # Display the price Gerald paid
    result = gerald_price
    return result

print(solution())