def solution():
    # Define the prices of ducks and chickens and the number of chickens sold
    duck_price = 10
    chicken_price = 8
    chickens_sold = 5

    # Calculate the farmer's earnings from selling chickens and ducks
    earnings = (chickens_sold * chicken_price) + (duck_price * x)

    # Calculate the cost of the wheelbarrow
    wheelbarrow_cost = earnings / 2

    # Calculate the amount the farmer received for selling the wheelbarrow
    wheelbarrow_sell = wheelbarrow_cost + 60

    # Solve for the number of ducks sold using the equation (earnings - wheelbarrow_cost)/2 = earnings - wheelbarrow_sell
    x = (wheelbarrow_sell - 3*earnings/2)/(duck_price-2*chicken_price)

    result = x
    return result

print(solution())