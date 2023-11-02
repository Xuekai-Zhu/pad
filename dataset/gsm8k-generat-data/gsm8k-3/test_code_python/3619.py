def solution():
    """In a restaurant, one cup of coffee is $6 and a piece of cheesecake $10. When buying them together, the client gets a 25% discount. What is the final price of such a set?"""
    # Define the prices of coffee and cheesecake
    COFFEE_PRICE = 6
    CHEESECAKE_PRICE = 10

    # Calculate the total cost of the set
    set_cost = COFFEE_PRICE + CHEESECAKE_PRICE

    # Apply the discount
    discount = set_cost * 0.25
    discounted_cost = set_cost - discount

    # Display the final cost
    result = discounted_cost
    return result

print(solution())