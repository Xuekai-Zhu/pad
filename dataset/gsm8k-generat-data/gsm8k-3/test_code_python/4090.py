def solution():
    """How much money did you make if you sold 220 chocolate cookies at $1 per cookie and 70 vanilla cookies at $2 per cookie?"""
    # Define the price per chocolate cookie
    CHOCOLATE_PRICE = 1

    # Define the price per vanilla cookie
    VANILLA_PRICE = 2

    # Define the number of chocolate and vanilla cookies sold
    chocolate_cookies = 220
    vanilla_cookies = 70

    # Calculate the total revenue from chocolate cookies
    chocolate_revenue = chocolate_cookies * CHOCOLATE_PRICE

    # Calculate the total revenue from vanilla cookies
    vanilla_revenue = vanilla_cookies * VANILLA_PRICE

    # Calculate the total revenue from all cookies
    total_revenue = chocolate_revenue + vanilla_revenue

    # Display the total revenue
    result = total_revenue
    return result

print(solution())