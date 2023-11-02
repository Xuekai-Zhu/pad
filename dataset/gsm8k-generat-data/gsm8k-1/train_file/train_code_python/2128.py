def solution():
    """A farmer is selling ducks and chickens at the market. He sells ducks for $10 and chickens for $8. He sells 5 chickens and some ducks. He then spends half his earnings on a new wheelbarrow. After buying it, someone sees it and agrees to pay the farmer double what the farmer paid and the farmer earns another $60. How many ducks did the farmer sell?"""
    duck_price = 10
    chicken_price = 8
    chickens_sold = 5
    total_earnings = (chickens_sold * chicken_price) + (duck_sold * duck_price)
    wheelbarrow_cost = total_earnings / 2
    remaining_earnings = total_earnings - wheelbarrow_cost - 60
    duck_sold = remaining_earnings / duck_price
    result = duck_sold
    return result

print(solution())