def solution():
    """There are many CDs in the store. The rock and roll CDs are $5 each, the pop CDs are $10 each, the dance CDs are $3 each, and the country CDs are $7 each. Julia wants to buy 4 of each, but she only has 75 dollars. How much money is she short?"""
    # Define the prices of each type of CD and the quantity that Julia wants to buy
    ROCK_PRICE = 5
    POP_PRICE = 10
    DANCE_PRICE = 3
    COUNTRY_PRICE = 7
    QUANTITY = 4

    # Calculate the total cost of 4 of each type of CD
    total_cost = (ROCK_PRICE + POP_PRICE + DANCE_PRICE + COUNTRY_PRICE) * QUANTITY

    # Calculate how much money Julia is short
    short_amount = total_cost - 75

    # Display how much money Julia is short
    result = short_amount
    return result

print(solution())