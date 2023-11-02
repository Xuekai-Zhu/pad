def solution():
    """Tommy's home is worth 25% more than he bought it for. He sells it and buys a new house that costs $500,000. If he had to take a loan for the 75% he can't pay, how much did he buy his first house for?"""
    # Calculate the amount Tommy paid as the down payment for his new house
    down_payment = 0.25 * 500000

    # Calculate the amount Tommy is financing through a mortgage for his new house
    mortgage_amount = 0.75 * 500000

    # Since the value of his old house was 25% more than what he bought it for, it means his old house was worth 125% of what he bought it for.
    # Let x be what he bought his old house for. Then 1.25x is the value of his old house.
    # Since he sold his old house, he must have received the value of his old house, which is 1.25x.
    # Therefore, 1.25x = down_payment + mortgage_amount
    # Solving for x gives x = (down_payment + mortgage_amount) / 1.25
    first_house_price = (down_payment + mortgage_amount) / 1.25

    # Display the price of the first house
    result = first_house_price
    return result

print(solution())