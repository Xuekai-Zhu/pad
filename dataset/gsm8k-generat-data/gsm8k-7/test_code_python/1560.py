def solution():
    budget = 60
    extra_cost = 0.2  # 20% more expensive
    smaller_frame_price_ratio = 0.75  # 3/4 of the original frame price

    # Calculate the price of the original frame
    original_frame_price = budget / (1 + extra_cost)

    # Calculate the price of the smaller frame
    smaller_frame_price = original_frame_price * smaller_frame_price_ratio

    # Calculate the amount of money Yvette remains with
    remaining_money = budget - smaller_frame_price
    result = remaining_money
    return result

print(solution())