def solution():
    """ Yvette wants to frame a new picture. When she goes to her local frame shop, she finds out that the frame she wanted is 20% more expensive than her budget of $60. If she paid for a smaller frame at 3/4 the new price of the frame she initially intended to buy, how much money did she remain with?"""
    # Define Yvette's budget and the price increase percentage
    BUDGET = 60
    PRICE_INCREASE_PERCENTAGE = 0.2

    # Calculate the price of the frame Yvette wanted
    original_price = BUDGET / (1 + PRICE_INCREASE_PERCENTAGE)
    new_price = original_price * (1 + PRICE_INCREASE_PERCENTAGE)

    # Calculate the price of the smaller frame Yvette purchased
    smaller_frame_price = 0.75 * new_price

    # Calculate how much money Yvette remained with
    remaining_money = BUDGET - smaller_frame_price

    # Display the remaining money
    result = remaining_money
    return result

print(solution())