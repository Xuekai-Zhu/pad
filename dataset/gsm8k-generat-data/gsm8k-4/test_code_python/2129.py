def solution():
    """A farmer is selling ducks and chickens at the market. He sells ducks for $10 and chickens for $8. He sells 5 chickens and some ducks. He then spends half his earnings on a new wheelbarrow. After buying it, someone sees it and agrees to pay the farmer double what the farmer paid and the farmer earns another $60. How many ducks did the farmer sell?"""
    # Define the selling prices of ducks and chickens
    duck_price = 10
    chicken_price = 8

    # Define the number of chickens sold
    chickens_sold = 5

    # Define the earnings before buying the wheelbarrow
    earnings_before_wheelbarrow = chickens_sold * chicken_price

    # Determine the number of ducks sold based on the total earnings
    for i in range(earnings_before_wheelbarrow // duck_price):
        ducks_sold = i
        total_earnings = earnings_before_wheelbarrow + (ducks_sold * duck_price)
        if total_earnings * 0.5 == duck_price * ducks_sold:
            # Calculate the double price for the wheelbarrow
            double_price = duck_price * ducks_sold * 2
            # Calculate the total earnings after selling the wheelbarrow
            total_earnings += double_price + 60
            # Calculate the number of ducks sold based on the total earnings
            ducks_sold = (total_earnings - earnings_before_wheelbarrow) // duck_price
            result = ducks_sold
            return result

print(solution())