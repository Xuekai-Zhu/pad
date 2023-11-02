def solution():
    """Yvette wants to frame a new picture. When she goes to her local frame shop, she finds out that the frame she wanted is 20% more expensive than her budget of $60. If she paid for a smaller frame at 3/4 the new price of the frame she initially intended to buy, how much money did she remain with?"""
    # Define the initial budget and the percentage increase in price
    initial_budget = 60
    percentage_increase = 0.2

    # Calculate the price of the frame Yvette initially wanted
    initial_price = initial_budget / (1 + percentage_increase)

    # Calculate the price of the smaller frame
    smaller_price = 0.75 * initial_price * (1 + percentage_increase)

    # Calculate how much money Yvette has remaining after purchasing the smaller frame
    remaining_money = initial_budget - smaller_price

    # return the result
    result = remaining_money
    return result

print(solution())