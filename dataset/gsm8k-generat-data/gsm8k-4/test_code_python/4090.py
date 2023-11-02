def solution():
    """How much money did you make if you sold 220 chocolate cookies at $1 per cookie and 70 vanilla cookies at $2 per cookie?"""
    # Define the prices and quantities of chocolate and vanilla cookies
    chocolate_price = 1
    chocolate_quantity = 220
    vanilla_price = 2
    vanilla_quantity = 70

    # Calculate the total earnings from selling chocolate cookies
    chocolate_earnings = chocolate_price * chocolate_quantity

    # Calculate the total earnings from selling vanilla cookies
    vanilla_earnings = vanilla_price * vanilla_quantity

    # Calculate the total earnings from selling all cookies
    total_earnings = chocolate_earnings + vanilla_earnings

    # return the result
    result = total_earnings
    return result

print(solution())