def solution():
    """Rose is an aspiring artist. She wants a paintbrush that costs $2.40, a set of paints that costs $9.20, and an easel that costs $6.50 so she can do some paintings. Rose already has $7.10. How much more money does Rose need?"""
    # Define the prices of the paintbrush, paints, and easel
    paintbrush_price = 2.40
    paints_price = 9.20
    easel_price = 6.50

    # Calculate the total cost of all the items
    total_cost = paintbrush_price + paints_price + easel_price

    # Calculate the amount of money Rose still needs
    money_needed = total_cost - 7.10

    # return the result
    result = money_needed
    return result

print(solution())