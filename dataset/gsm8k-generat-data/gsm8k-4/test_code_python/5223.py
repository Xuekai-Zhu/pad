def solution():
    """Spongebob works in a burger shop. If he sells 30 burgers for $2 each and 12 large fries for $1.5. How much will Spongebob earn for the day?"""
    # Define the prices of burgers and fries
    burger_price = 2
    fries_price = 1.5

    # Calculate the earnings from selling burgers
    burger_earnings = 30 * burger_price

    # Calculate the earnings from selling fries
    fries_earnings = 12 * fries_price

    # Calculate the total earnings for the day
    total_earnings = burger_earnings + fries_earnings

    # return the result
    result = total_earnings
    return result

print(solution())