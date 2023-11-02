def solution():
    """A farmer is selling ducks and chickens at the market. He sells ducks for $10 and chickens for $8. He sells 5 chickens and some ducks. He then spends half his earnings on a new wheelbarrow. After buying it, someone sees it and agrees to pay the farmer double what the farmer paid and the farmer earns another $60. How many ducks did the farmer sell?"""
    duck_price = 10
    chicken_price = 8
    num_chickens_sold = 5

    # Find the total earnings from selling chickens and some ducks
    total_earnings = num_chickens_sold * chicken_price
    remaining_earnings = total_earnings
    num_ducks_sold = 0

    # Try selling different number of ducks until the earnings are split in half
    while remaining_earnings >= total_earnings / 2:
        num_ducks_sold += 1
        remaining_earnings = (num_ducks_sold * duck_price) + (num_chickens_sold * chicken_price)

    # Calculate the cost of the wheelbarrow and earnings from selling it
    wheelbarrow_cost = remaining_earnings / 2
    earnings_from_wheelbarrow = wheelbarrow_cost + 60

    # Calculate the number of ducks sold
    num_ducks_sold += (earnings_from_wheelbarrow - remaining_earnings) / duck_price

    result = num_ducks_sold
    return result

print(solution())