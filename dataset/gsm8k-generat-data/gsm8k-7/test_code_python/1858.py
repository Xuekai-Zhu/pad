def solution():
    total_price = 600000
    expensive_price = total_price * 2 / 3  # Second house is twice as expensive as the first and over budget
    affordable_price = total_price / 3  # Combined price of both houses is $600,000

    # Calculate the price of the house they bought
    bought_price = affordable_price

    result = bought_price
    return result

print(solution())