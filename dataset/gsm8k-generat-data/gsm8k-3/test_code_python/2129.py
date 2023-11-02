def solution():
    """A farmer is selling ducks and chickens at the market. He sells ducks for $10 and chickens for $8. He sells 5 chickens and some ducks. He then spends half his earnings on a new wheelbarrow. After buying it, someone sees it and agrees to pay the farmer double what the farmer paid and the farmer earns another $60. How many ducks did the farmer sell?"""
    # Define the price of a duck and a chicken
    DUCK_PRICE = 10
    CHICKEN_PRICE = 8

    # Define the number of chickens sold and the total earnings
    chickens_sold = 5
    total_earnings = chickens_sold * CHICKEN_PRICE

    # Calculate the number of ducks sold
    for i in range(0, 101):
        ducks_sold = i
        earnings_from_ducks = ducks_sold * DUCK_PRICE
        if total_earnings + earnings_from_ducks == (total_earnings + earnings_from_ducks) / 2 + 60:
            break

    # Display the number of ducks sold
    result = ducks_sold
    return result

print(solution())